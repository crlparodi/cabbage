
## Tasks to operate as API
# Register User - OK
# List Users - OK
# Delete User - OK
# Update User as Babysitter - OK
# List Babysitter - OK
# Get Babysitter - OK
# Update Babysitter - OK
# Delete Babysitter (by Retrograde user) - OK
# Delete Babysitter (by Removing Babysitter) - OK

from apps.api.tasks import create_member, update_member

from apps.auth.accounts.models import Member
from apps.auth.babysitters.models import Babysitter
from apps.auth.babysitters import components
from rest_framework import serializers
from rest_framework.reverse import reverse
from django.core.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['email', 'full_name', 'is_babysitter', 'is_staff']

class MemberListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='member-detail',
        lookup_field='email'
    )

    class Meta:
        model = Member
        fields = ['url', 'email', 'full_name', 'is_babysitter', 'is_staff']

class MemberBabysitterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='member-detail',
        lookup_field='email'
    )

    class Meta:
        model = Member
        fields = ['url', 'email', 'full_name']
        lookup_field = 'email'

class MemberBabysitterUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['full_name']

class MemberCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='member-detail',
        lookup_field='email'
    )
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def create(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        member = {
            'email': self.validated_data['email'],
            'full_name': self.validated_data['full_name'],
            'is_babysitter': self.validated_data['is_babysitter'],
            'is_staff': self.validated_data['is_staff']
        }

        if password != password2:
            return serializers.ValidationError({"password": "Passwords must match."})

        create_member.apply_async((member, password))

    class Meta:
        model = Member
        fields = ['url', 'email', 'full_name', 'password', 'password2', 'is_babysitter', 'is_staff']

class MemberUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='member-detail',
        lookup_field='email'
    )
    full_name = serializers.CharField(required=False, source="member.full_name")
    is_babysitter = serializers.BooleanField(required=False, default=False)
    is_staff = serializers.BooleanField(required=False, default=False)

    def update(self, member=None):
        if member is not None:
            member_data = {
                'email': member.get_short_name(),
                'is_babysitter': self.validated_data['is_babysitter'],
                'is_staff': self.validated_data['is_staff']
            }
        else:
            raise ValidationError
        
        update_member.apply_async((member_data,))

    class Meta:
        model = Member
        fields = ['url', 'full_name', 'is_babysitter', 'is_staff']

class BabysitterSerializer(serializers.ModelSerializer):
    member = MemberBabysitterSerializer()

    class Meta:
        model = Babysitter
        fields = ['member', 'location', 'birth_date', 'age_target', 'time_target', 'phone']

class BabysitterHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'member__email': obj.member.email
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

class BabysitterListSerializer(serializers.HyperlinkedModelSerializer):
    member = MemberBabysitterSerializer()
    url = BabysitterHyperlinkIdentityField(view_name='babysitter-detail')

    class Meta:
        model = Babysitter
        fields = ['url', 'member', 'location', 'birth_date', 'age_target', 'time_target', 'phone']
        lookup_field = 'member__email'
        lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'


class BabysitterUpdateSerializer(serializers.ModelSerializer):
    location = serializers.ChoiceField(required=False, choices=components.LOCATIONS, allow_blank=True)
    birth_date = serializers.DateField(required=False)
    age_target = serializers.ChoiceField(required=False, choices=components.AGE_TARGET_CHOICES, allow_blank=True)
    time_target = serializers.ChoiceField(required=False, choices=components.TIME_TARGET_CHOICES, allow_blank=True)
    phone = PhoneNumberField(required=False, region="FR", default="0600000000")

    def update(self, member=None):
        if member is not None:
            babysitter = Babysitter.objects.filter(member=member).get()
            if babysitter is not None:
                babysitter.location = self.validated_data.get('location', babysitter.location)
                babysitter.birth_date = self.validated_data.get('birth_date', babysitter.birth_date)
                babysitter.age_target = self.validated_data.get('age_target', babysitter.age_target)
                babysitter.time_target = self.validated_data.get('time_target', babysitter.time_target)
                babysitter.phone = self.validated_data.get('phone', babysitter.phone)
                babysitter.save()
            else:
                raise ValidationError
        else:
            raise ValidationError

        return babysitter

    class Meta:
        model = Babysitter
        fields = ['location', 'birth_date', 'age_target', 'time_target', 'phone']

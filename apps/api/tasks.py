from celery import shared_task

from apps.auth.accounts.models import Member
from apps.auth.babysitters.models import Babysitter

from django.core.exceptions import ValidationError

@shared_task
def create_member(member, password):
    obj = Member(
        email = member['email'],
        full_name = member['full_name'],
        is_babysitter = member['is_babysitter'],
        is_staff = member['is_staff']
    )
    obj.set_password(password)
    obj.save()
    return member

@shared_task
def update_member(member_data):
    member = Member.objects.get(email=member_data['email'])

    if member is not None:
        member.is_babysitter = member_data['is_babysitter']
        member.is_staff = member_data['is_staff']
    else:
        raise ValidationError

    member.save()

    if member.is_babysitter is True and not Babysitter.objects.filter(member_id=member.pk):
        Babysitter.objects.create(member_id=member.pk)

    if member.is_babysitter is False and Babysitter.objects.filter(member_id=member.pk):
        Babysitter.objects.get(member_id=member.pk).delete()
        
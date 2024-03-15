from django.core.exceptions import ValidationError

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from apps.auth.accounts.models import Member
from apps.auth.babysitters.models import Babysitter
from apps.auth.accounts.serializers import (
    MemberSerializer,
    MemberListSerializer,
    MemberCreateSerializer,
    MemberUpdateSerializer,
    BabysitterSerializer,
    BabysitterListSerializer,
    BabysitterUpdateSerializer
)

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    lookup_field='email'
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    def get_queryset(self):
        return Member.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'create':
            return MemberCreateSerializer
        if self.action == 'update':
            return MemberUpdateSerializer
        if self.action == 'list':
            return MemberListSerializer
        return MemberSerializer
 
    def create(self, request):
        serializer = MemberCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.create()
            data['response'] = "Member successfully created."
        else:
            data = serializer.errors
        return Response(data)

    def update(self, request, email):
        serializer = MemberUpdateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            try:
                serializer.update(Member.objects.filter(email=email).get())
                data['response'] = "Member successfully updated."
            except ValidationError:
                data['response'] = "Member does not exist."
        else:
            data = serializer.errors
        return Response(data)

    def partial_update(self, request, email=None):
        serializer = MemberUpdateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            try:
                serializer.update(Member.objects.filter(email=email).get())
                data['response'] = "Member successfully updated."
            except ValidationError:
                data['response'] = "Member does not exist."
        else:
            data = serializer.errors
        return Response(data)

class BabysitterViewSet(viewsets.ModelViewSet, mixins.RetrieveModelMixin):
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    lookup_field='member__email'
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    def get_queryset(self):
        return Babysitter.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'list':
            return BabysitterListSerializer
        if self.action == 'update':
            return BabysitterUpdateSerializer
        if self.action == 'partial_update':
            return BabysitterUpdateSerializer
        return BabysitterSerializer

    def update(self, request, member__email):
        serializer = BabysitterUpdateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            try:
                member = Member.objects.filter(email=member__email).get()
                serializer.update(member)
                data['response'] = "Babysitter successfully updated."
            except ValidationError:
                data['response'] = "Babysitter does not exist."
        else:
            data = serializer.errors
        return Response(data)

    def partial_update(self, request, member__email):
        serializer = BabysitterUpdateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            try:
                member = Member.objects.filter(email=member__email).get()
                serializer.update(member)
                data['response'] = "Babysitter successfully updated."
            except ValidationError:
                data['response'] = "Babysitter does not exist."
        else:
            data = serializer.errors
        return Response(data)
    
    def delete(self, request, member__email):
        serializer = MemberUpdateSerializer(email=member__email, is_babysitter=False)
        data = {}
        if serializer.is_valid():
            try:
                serializer.update()
                data['response'] = "Babysitter successfully removed."
            except ValidationError:
                data['response'] = "Babysitter does not exist."
        else:
            data = serializer.errors
        return Response(data)


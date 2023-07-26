# views CRM
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, mixins, filters
from crm.permissions import IsContactOrAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from crm.serializers import (
    ContractSerializer,
    ContractListSerializer,
    ClientSerializer,
    ClientListSerializer,
    EventSerializer,
    EventListSerializer
)

from crm.models import Contract, Client, Event


class ContractViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet
                      ):
    """
    API endpoint that allows contract to be listed by user authenticated
    and where user is attached, to be viewed, edited, or created a new
    one.
    """
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^client__company_name', '^client__last_name', '^email', 'date_created']
    # ordering_fields = ['client.company_name']
    queryset = Contract.objects.all()
    permission_classes = [IsContactOrAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return super().get_serializer_class()


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet
                    ):
    """
    API endpoint that allows Client to be listed by user authenticated
    and where user is attached, to be viewed, edited, or created a new
    one.
    """
    serializer_class = ClientSerializer
    list_serializer_class = ClientListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^client__company_name', '^client__last_name', '^email', 'date_created']
    # ordering_fields = ['client.company_name']
    queryset = Client.objects.all()
    permission_classes = [IsContactOrAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return super().get_serializer_class()

    @action(detail=True, methods=['post'])
    def signed(self, request, pk=None):
        client = self.get_object()
        client.existing = True
        client.save()
        message = f"{_('status')}: {_('contract signed!!')}"
        return Response(message)


class EventViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet
                   ):
    """
    API endpoint that allows Event to be listed by user authenticated
    and where user is attached, to be viewed, edited, or created a new
    one.
    """
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^contract__client__company_name', '^contract__client__last_name', 'date_created',
                     'contract__client__sales_contact__username', 'event_date', 'event_status',
                     '^support_user__username', 'contract__id'
                     ]
    queryset = Event.objects.all()
    permission_classes = [IsContactOrAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return super().get_serializer_class()

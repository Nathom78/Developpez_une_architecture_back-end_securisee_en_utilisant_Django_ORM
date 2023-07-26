from django.utils import timezone
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from crm.models import (
    Contract,
    Client,
    Event
)
from django.contrib.auth import get_user_model


class ContractListSerializer(serializers.ModelSerializer):
    """
    The contract List Serializer.
    Client and sale_contact is represented by the __str__ function.
    """
    client = serializers.StringRelatedField()
    sales_contact = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='contract-detail'
    )

    class Meta:
        model = Contract
        fields = ["sales_contact", "status", "client", 'id']


class ContractSerializer(serializers.ModelSerializer):
    """
    The contract serializer for retrieving or editing.
    Client and sale_contact is represented by the __str__ function.
    """

    sales_contact = serializers.StringRelatedField()
    date_created = serializers.DateField(default=serializers.CreateOnlyDefault(timezone.now().date()))

    def to_internal_value(self, data):
        print(data['client'])
        try:
            client_full_name = data['client']
            client_complex = client_full_name.split()
            print(client_complex)
            client_first_name = client_complex[0]
            client_last_name = client_complex[1]
            client = Client.objects.get(
                Q(first_name=client_first_name) &
                Q(last_name=client_last_name)
            )
            data['client'] = client.id
            print(client.id)
        finally:
            return super().to_internal_value(data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        client = Client.objects.get(pk=ret['client'])
        ret['client'] = str(client)
        return ret

    class Meta:
        model = Contract
        fields = ["id", "sales_contact", "client", "status", "amount", "payment_due", "date_created", "date_updated"]
        depth = 0
        validators = [
            UniqueTogetherValidator(
                queryset=Contract.objects.all(),
                fields=["client", "date_created"],
                message=_("There can only be one contract per client and per day.")
            )
        ]


class ClientListSerializer(serializers.ModelSerializer):
    """
    The Client List Serializer.
    Sale_contact is represented by the __str__ function.
    """
    sales_contact = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='client-detail'
    )

    class Meta:
        model = Client
        fields = ["full_name", "company_name", "sales_contact", "existing", 'id']


class ClientSerializer(serializers.ModelSerializer):
    """
    The Client serializer for retrieving or editing.
    Sale_contact is represented by the __str__ function.
    """
    sales_contact = serializers.SlugRelatedField(slug_field="username", queryset=get_user_model().objects.all())
    full_name = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = '__all__'
        depth = 0
        validators = [
            UniqueTogetherValidator(
                queryset=Client.objects.all(),
                fields=["first_name", "last_name", "company_name"]
            )
        ]


class EventListSerializer(serializers.ModelSerializer):
    """
    The contract List Serializer.
    Client, Contract and support_user is represented by the __str__ function.
    """
    contract = serializers.SlugRelatedField(slug_field="contract_name", read_only=True)
    client = serializers.StringRelatedField()
    support_user = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='event-detail'
    )

    class Meta:
        model = Event
        fields = ["client", "support_user", "event_status", "contract", "id"]


class EventSerializer(serializers.ModelSerializer):
    """
    The contract serializer for retrieving or editing.
    Client, Contract and support_user is represented by the __str__ function.
    """
    # contract = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    support_user = serializers.SlugRelatedField(slug_field="username", queryset=get_user_model().objects.all())

    def to_internal_value(self, data):
        name = gettext("Contract")
        on = gettext("of")
        try:
            contract_name = data['contract']
            client_complex = contract_name.split(f"{name}: ")
            client_inlist = client_complex[1].split(f" {on} ")
            client_first_name = client_inlist[0].split()[0]
            client_last_name = client_inlist[0].split()[1]
            contract = Contract.objects.get(
                Q(client__first_name=client_first_name) &
                Q(client__last_name=client_last_name) &
                Q(date_created=client_inlist[1])
            )
            data['contract'] = contract.id
        finally:
            return super().to_internal_value(data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        contract = Contract.objects.get(pk=ret['contract'])
        ret['contract'] = str(contract)
        return ret

    def validate(self, data):
        if data['event_date'] < timezone.now().date():
            raise serializers.ValidationError({"Event": _("Date mustn't in the past")})
        return data

    class Meta:
        model = Event
        fields = ["id", "contract", "client", "support_user", "attendees", "location", "note", "event_status",
                  "event_date", "date_created", "date_updated"]

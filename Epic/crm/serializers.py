from rest_framework import serializers

from crm.models import (
    Contract,
    Client,
    Event
)


class ContractListSerializer(serializers.ModelSerializer):
    """
    The contract List Serializer.
    Client and sale_contact is represented by the __str__ function.
    """
    client = serializers.StringRelatedField()
    sales_contact = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        # many=True,
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
    client = serializers.StringRelatedField()
    sales_contact = serializers.StringRelatedField()

    class Meta:
        model = Contract
        fields = '__all__'
        depth = 0


class ClientListSerializer(serializers.ModelSerializer):
    """
    The Client List Serializer.
    Sale_contact is represented by the __str__ function.
    """
    sales_contact = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        # many=True,
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
    sales_contact = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = '__all__'
        depth = 0


class EventListSerializer(serializers.ModelSerializer):
    """
    The contract List Serializer.
    Client, Contract and support_user is represented by the __str__ function.
    """
    contract = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    support_user = serializers.StringRelatedField()
    id = serializers.HyperlinkedRelatedField(
        # many=True,
        read_only=True,
        view_name='event-detail'
    )

    class Meta:
        model = Event
        fields = ["support_user", "event_status", "client", "contract", "id"]


class EventSerializer(serializers.ModelSerializer):
    """
    The contract serializer for retrieving or editing.
    Client, Contract and support_user is represented by the __str__ function.
    """
    contract = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    support_user = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'
        depth = 0

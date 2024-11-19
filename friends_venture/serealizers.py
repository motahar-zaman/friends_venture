from rest_framework import serializers
from models.models.partners import Partner
from models.models.transactions import Transaction
import ipdb


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'nick_name', 'email')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #
    #     try:
    #         ipdb.set_trace()
    #         data['created_at'] = data['created_at'].strftime("%m/%d/%Y, %H:%M:%S")
    #     except KeyError:
    #         pass
    #
    #     return data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

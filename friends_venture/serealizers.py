from rest_framework import serializers
from models.models.partners import Partner
from models.models.transactions import Transaction
import ipdb


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'nick_name', 'email')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['created_at'] = instance.created_at.strftime("%d/%m/%Y, %H:%M:%S")
        except KeyError:
            pass

        return data


class PartnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['created_at'] = instance.created_at.strftime("%d/%m/%Y, %H:%M:%S")
            transactions = []
            for item in instance.transactions.all():
                transactions.append({
                    'type': item.type,
                    'amount': item.amount,
                    'date': item.date.strftime("%d/%m/%Y"),
                    'given_by': item.given_by,
                    'purpose': item.purpose,
                    'updated_by': item.updated_by,
                    'note': item.note,
                    'created_at': item.created_at.strftime("%d/%m/%Y, %H:%M:%S")
                })
            data['transactions'] = transactions
        except KeyError:
            pass

        return data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['created_at'] = instance.created_at.strftime("%m/%d/%Y, %H:%M:%S")
            data['partner'] = {
                'id': instance.partner.id,
                'nick_name': instance.partner.nick_name,
                'first_name': instance.partner.first_name,
                'last_name': instance.partner.last_name
            }
        except KeyError:
            pass

        return data

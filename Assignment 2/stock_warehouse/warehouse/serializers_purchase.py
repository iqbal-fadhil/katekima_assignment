from rest_framework import serializers
from .models_purchase import PurchaseHeader, PurchaseDetail
from .models_item import Item

#This is serializer for the Purchase models.
class PurchaseHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHeader
        fields = ['code', 'date', 'description']

class PurchaseDetailSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(write_only=True)
    header_code = serializers.CharField(write_only=True)

    class Meta:
        model = PurchaseDetail
        fields = ['item_code', 'quantity', 'unit_price', 'header_code']

    def create(self, validated_data):
        item_code = validated_data.pop('item_code')
        header_code = validated_data.pop('header_code')

        item = Item.objects.get(code=item_code, is_deleted=False)
        header = PurchaseHeader.objects.get(code=header_code, is_deleted=False)

        # Update stock and balance
        item.stock += validated_data['quantity']
        item.balance += validated_data['quantity'] * validated_data['unit_price']
        item.save()

        return PurchaseDetail.objects.create(item=item, header=header, **validated_data)

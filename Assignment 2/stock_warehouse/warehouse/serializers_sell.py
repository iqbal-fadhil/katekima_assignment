from rest_framework import serializers
from .models_sell import SellHeader, SellDetail
from .models_item import Item

#This is serializer for the Sale models.
class SellHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellHeader
        fields = '__all__'

class SellDetailSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(write_only=True)
    header_code = serializers.CharField(write_only=True)

    class Meta:
        model = SellDetail
        fields = ['item_code', 'quantity', 'header_code']

    def create(self, validated_data):
        item_code = validated_data.pop('item_code')
        header_code = validated_data.pop('header_code')

        item = Item.objects.get(code=item_code, is_deleted=False)
        header = SellHeader.objects.get(code=header_code, is_deleted=False)

        quantity = validated_data['quantity']

        # Check stock
        if item.stock < quantity:
            raise serializers.ValidationError("Not enough stock available.")

        # Average price method
        average_price = item.balance / item.stock if item.stock > 0 else 0

        # Reduce stock and balance
        item.stock -= quantity
        item.balance -= average_price * quantity
        item.save()

        # Inject actual ForeignKeys into validated_data
        validated_data['item'] = item
        validated_data['header'] = header

        return SellDetail.objects.create(**validated_data)

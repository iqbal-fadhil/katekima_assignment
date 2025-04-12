from rest_framework import serializers
from .models_sell import SellHeader, SellDetail

class SellHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellHeader
        fields = '__all__'

class SellDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellDetail
        fields = '__all__'

    def create(self, validated_data):
        detail = super().create(validated_data)
        item = detail.item
        quantity = detail.quantity

        # Decrease stock and balance
        if item.stock < quantity:
            raise serializers.ValidationError("Not enough stock available.")

        average_price = item.balance / item.stock if item.stock > 0 else 0
        item.stock -= quantity
        item.balance -= average_price * quantity
        item.save()
        return detail
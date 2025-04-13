from rest_framework import serializers
from .models_item import Item

#This is serializer for the Item model.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['code', 'name', 'unit', 'description', 'stock', 'balance']
        read_only_fields = ['stock', 'balance']

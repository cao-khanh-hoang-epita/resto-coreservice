from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'description', 'stocks', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

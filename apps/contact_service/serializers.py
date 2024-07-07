from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    stocks = serializers.IntegerField()

    # We don't need to implement create() or update() methods
    # as this serializer is only used for validation and data shaping

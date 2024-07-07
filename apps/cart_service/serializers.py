from rest_framework import serializers

class CartItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    menu_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    items = CartItemSerializer(many=True)
    total = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cart_id = serializers.IntegerField()
    status = serializers.CharField(read_only=True)
    total = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

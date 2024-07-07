from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .connector import cart_service_request
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer

class CartView(APIView):
    def get(self, request):
        cart = cart_service_request('GET', '/api/cart/')
        serializer = CartSerializer(data=cart)
        serializer.is_valid()
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            updated_cart = cart_service_request('POST', '/api/cart/', data=serializer.validated_data)
            return Response(updated_cart, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartItemView(APIView):
    def put(self, request, item_id):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            updated_item = cart_service_request('PUT', f'/api/cart/{item_id}/', data=serializer.validated_data)
            return Response(updated_item)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        cart_service_request('DELETE', f'/api/cart/{item_id}/')
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = cart_service_request('POST', '/api/order/', data=serializer.validated_data)
            return Response(order, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, order_id):
        order = cart_service_request('GET', f'/api/order/{order_id}/')
        serializer = OrderSerializer(data=order)
        serializer.is_valid()
        return Response(serializer.data)

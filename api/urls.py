from django.urls import path, include

urlpatterns = [
    path('api/menu/', include('apps.menu.urls')),    # Route to menu service
    path('api/cart/', include('apps.cart.urls')),    # Route to cart service
    # Add more routes as needed for other microservices
]

from django.urls import path
from .views import deleteproduct, productlist, saveuser, updateproduct

urlpatterns = [
    path("deleteproduct/<int:product_id>/", deleteproduct, name="deleteproduct"),
    path("productlist/", productlist, name="productlist"),
    path("saveuser/", saveuser),
    path("updateproduct/<int:product_id>/", updateproduct, name="updateproduct"),
]
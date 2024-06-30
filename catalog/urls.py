from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, ProductCreateView, \
    ProductDeleteView, ProductUpdateView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('category', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
# path('create/', BlogCreateView.as_view(), name='create'),
#     path('', BlogListView.as_view(), name='list'),
#     path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
#     path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
#     path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]

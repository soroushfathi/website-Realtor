from django.urls import path, re_path
from .views import index, index_items, detail, search

# app_name = 'listings'
urlpatterns = [
    path('', index, name='listing'),
    path('items', index_items, name='listings_items'),
    # path('<int:listing_id>', detail, name='detail'),
    re_path(r'^(?P<listing_id>\d+)/$', detail, name='detail'),
    path('search', search, name='search')
]
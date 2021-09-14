from django.contrib import admin
from .models import Listings 

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','is_sold','is_published','price',)
    list_filter = ('is_published',)
    list_per_page = 8


admin.site.register(Listings, ListingAdmin)

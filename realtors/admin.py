from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    list_display_links = ('name', 'email')
    # list_editable = ('')

admin.site.register(Realtor, RealtorAdmin)

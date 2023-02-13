from django.contrib import admin
from .models import Item



class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_description')


    def get_description(self, obj):
        return obj.description[0:50] 
    get_description.admin_order_field = 'description'
    get_description.short_description = 'description'


admin.site.register(Item, ItemAdmin)

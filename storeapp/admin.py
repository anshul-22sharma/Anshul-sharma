from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


class AdminProduct(admin.ModelAdmin):

	list_display = ['name','price','category']


class AdminCategory(admin.ModelAdmin):

	list_display = ['name']



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
# admin.site.register(Session)
admin.site.register(Session, SessionAdmin)



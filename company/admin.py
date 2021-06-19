from django.contrib import admin
from .models import Company, Client

class CompanyAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['name', 'location', 'phone', 'created_at', 'update_at']
admin.site.register(Company, CompanyAdmin)

class ClientAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['company', 'name', 'location']    
admin.site.register(Client, ClientAdmin)

# Register your models here.

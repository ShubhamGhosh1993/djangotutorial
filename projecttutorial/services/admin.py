from django.contrib import admin
from services.models import Services

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=("id","service_icon","service_title","service_desc")
    
admin.site.register(Services,ServiceAdmin)
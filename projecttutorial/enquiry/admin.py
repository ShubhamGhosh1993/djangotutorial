from django.contrib import admin

# Register your models here.
from enquiry.models import Enquiry

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("enquiry_title", "enquiry_desc")
    
admin.site.register(Enquiry, EnquiryAdmin)
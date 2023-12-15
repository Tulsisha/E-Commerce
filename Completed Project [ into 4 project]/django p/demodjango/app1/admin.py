from django.contrib import admin
from app1.models import contactform
admin.site.register(contactform)
from app1.models import CPersonM
admin.site.register(CPersonM)
# Register your models here.
from app1.models import CPersonM2
admin.site.register(CPersonM2)
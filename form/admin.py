from django.contrib import admin
from .models import FormModel

class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

admin.site.register(FormModel, FormAdmin)
# Register your models here.

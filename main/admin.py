from django.contrib import admin
from main.models import Cake


@admin.register(Cake)
class PersonAdmin(admin.ModelAdmin):
    pass
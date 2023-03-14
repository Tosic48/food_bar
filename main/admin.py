from django.contrib import admin
from main.models import Сakes


@admin.register(Сakes)
class PersonAdmin(admin.ModelAdmin):
    pass
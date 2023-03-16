from django.contrib import admin
from main.models import Cakes


@admin.register(Cakes)
class PersonAdmin(admin.ModelAdmin):
    pass
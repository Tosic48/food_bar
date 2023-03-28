from django.contrib import admin
from main.models import Cakes, Review


@admin.register(Cakes)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class PersonAdmin(admin.ModelAdmin):
    pass
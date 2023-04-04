from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models import Cakes, Review


@admin.register(Cakes)
class PersonAdmin(admin.ModelAdmin):
    fields = ('title', 'composition', 'price', 'rating', 'vegetarion_type', 'layer_number', 'photo', 'preview_photo')
    readonly_fields = ('preview_photo',)
    list_display = ('pk', 'title', 'composition', 'price', 'vegetarion_type')
    list_display_links = ('title',)
    list_editable = ('vegetarion_type', 'price',)
    list_filter = ('vegetarion_type',)
    search_fields = ('composition',)


    def preview_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="150" />')


@admin.register(Review)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'customers', 'text', 'details')
    list_display_links = ('customers',)


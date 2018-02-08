from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact, Talk


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1
class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html(f'<a href="{obj.website}">{obj.website}</a>')

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html(f'<img width="32px" src="{obj.photo}" />')

    photo_img.short_description = 'foto'

admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
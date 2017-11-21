from django.contrib import admin

from .models import *

class ExcerptInline(admin.TabularInline):
    model = Excerpt


class WomenAdmin(admin.ModelAdmin):
    inlines = [ExcerptInline]


admin.site.register(Images)
# admin.site.register(Themes)
# admin.site.register(Excerpt)
admin.site.register(Women, WomenAdmin)
admin.site.register(Location)

admin.site.site_header = 'History Moves Admin'

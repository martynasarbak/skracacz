from django.contrib import admin
from .models import URL


# admin.site.register(URL)

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):

    list_display = ('shortened_url', 'original_url')
from django.contrib import admin

from .models import Server, ServerGroup

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'group')

admin.site.register(Server, ServerAdmin)
admin.site.register(ServerGroup)
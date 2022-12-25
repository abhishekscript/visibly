
from django.contrib import admin

from kubecmd import models

# This will make application visible in admin panel
class SystemApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(models.SystemApplication, SystemApplicationAdmin)
admin.site.register(models.SystemApplicationInQueue, SystemApplicationAdmin)
admin.site.register(models.SystemApplicationConfig, SystemApplicationAdmin)


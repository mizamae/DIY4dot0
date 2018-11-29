from django.contrib import admin

from releases.models import ReleaseModel



class ReleaseModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ReleaseModel,ReleaseModelAdmin)

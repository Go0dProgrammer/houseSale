from django.contrib import admin
from .models import Ad


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Ad, PostAdmin)


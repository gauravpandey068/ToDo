from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'created_on')
    search_fields = ('task', 'user', 'created_on')


admin.site.register(Todo, TodoAdmin)

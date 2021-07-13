from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('names', 'last_name','is_staff','is_active')
    list_filter = ('is_staff','is_active')
    search_fields = ['last_name']

admin.site.register(User, UserAdmin)

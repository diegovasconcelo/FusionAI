from django.contrib import admin

from .models import Home, Subscriber, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message', 'created','modified')
    list_filter = ['full_name']
    search_fields = ['email']

admin.site.register(Contact, ContactAdmin)

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'web', 'repository', 'created', 'modified')
    search_fields = ['title']

admin.site.register(Home, HomeAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    search_fields = ['email']

admin.site.register(Subscriber, SubscriberAdmin)
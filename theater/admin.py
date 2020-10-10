from django.contrib import admin
from .models import theater_list
from .models import contacts

admin.site.register(theater_list)
admin.site.register(contacts)


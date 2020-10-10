from django.contrib import admin
from .models import Profile, Ticket, Payment


admin.site.register(Profile)
admin.site.register(Ticket)
admin.site.register(Payment)

from django.contrib import admin
from .models import Project, Role, User, Ticket

# Register your models here.
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Ticket)
# admin.site.register(Ticket_Assignment)

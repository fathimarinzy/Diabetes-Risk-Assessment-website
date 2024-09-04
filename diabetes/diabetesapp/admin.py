from django.contrib import admin
from . models import user,feedback,Info,doctor,appointments

# Register your models here.
admin.site.register(user)
admin.site.register(feedback)
admin.site.register(Info)
admin.site.register(doctor)
admin.site.register(appointments)
from django.contrib import admin
from .models import Babysitter

# Register your models here.


@admin.register(Babysitter)
class BabysitterAdmin(admin.ModelAdmin):
    list_display = ('member', 'location', 'birth_date', 'age_target', 'time_target', 'phone', )

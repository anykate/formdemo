from django.contrib import admin
from .models import Preference


# Register your models here.
@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    pass

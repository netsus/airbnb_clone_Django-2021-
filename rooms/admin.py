from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomdAdmin(admin.ModelAdmin):

    pass
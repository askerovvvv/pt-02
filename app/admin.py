from django.contrib import admin

from app.models import GameInformation, Category

# Register your models here.
admin.site.register(GameInformation)
admin.site.register(Category)
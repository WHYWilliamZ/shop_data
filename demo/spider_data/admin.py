from django.contrib import admin
from .models import Data

from django.contrib import admin


@admin.register(Data)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','addr','phone']



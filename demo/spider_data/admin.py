from django.contrib import admin
from .models import Data

from django.contrib import admin


@admin.register(Data)
class ShopDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_name','shop_addr','aver_price','shop_star','comment_count']



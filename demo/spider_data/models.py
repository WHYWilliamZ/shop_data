from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=20, verbose_name='商铺名字')
    addr = models.CharField(max_length=50,verbose_name='商铺地址')
    phone = models.CharField(max_length=11,verbose_name='联系电话')

    class Meta:
        db_table = 'shop_data'
        verbose_name = '店铺数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



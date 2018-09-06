from django.db import models


class Data(models.Model):
    shop_name = models.CharField(max_length=50, verbose_name='健身房名字')
    shop_addr = models.CharField(null=True,max_length=50,verbose_name='健身房地址')
    aver_price = models.CharField(max_length=10,null=True,verbose_name='平均价格')
    shop_star = models.CharField(null=True,max_length= 10,verbose_name='星级')
    comment_count = models.IntegerField(default=0,verbose_name='评论数量')

    class Meta:
        db_table = 'shop_data'
        verbose_name = '健身房数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Item(models.Model):
    '''商品'''
    name = models.CharField(max_length=100, verbose_name='商品名')
    price = models.IntegerField(verbose_name='価格')
    # 画像をアップロードするためのフィールド, Pillowをインストールしている場合は、ImageFieldを使用することができます。
    image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name='画像')

    class Meta:
        verbose_name = verbose_name_plural = '商品'

    def __str__(self):
        return f'{self.name} ({self.price}円)'


class Topping(models.Model):
    '''トッピング'''
    name = models.CharField(max_length=100, verbose_name='トッピング名')
    price = models.IntegerField(verbose_name='価格')

    class Meta:
        verbose_name = verbose_name_plural = 'トッピング'

    def __str__(self):
        return f'{self.name} ({self.price}円)'


class ToppingOrder(models.Model):
    '''トッピング注文'''
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='topping_orders', verbose_name='注文')
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE, verbose_name='トッピング')
    quantity = models.IntegerField(verbose_name='数量', validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = verbose_name_plural = 'トッピング注文'

    def __str__(self):
        return f'{self.topping} x {self.quantity}'


class Order(models.Model):
    '''注文'''
    table_no = models.PositiveSmallIntegerField(
        verbose_name='テーブル番号', validators=[MinValueValidator(1), MaxValueValidator(10)])
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='商品')
    toppings = models.ManyToManyField(Topping, through=ToppingOrder, blank=True, verbose_name='トッピング')
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name='注文日時')

    class Meta:
        verbose_name = verbose_name_plural = '注文'

    def __str__(self):
        return f'{self.item} {list(self.topping_orders.all())}'

    @property
    def total_price(self):
        '''合計金額'''
        return self.item.price + sum(topping_order.topping.price * topping_order.quantity for topping_order in self.topping_orders.all())
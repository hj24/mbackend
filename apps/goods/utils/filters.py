import django_filters
from rest_framework import filters

from ..models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    # 模糊查询，前缀i表示忽略大小写
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']


class OrderingFilter(filters.OrderingFilter):

    ordering_param = 'o'
    ordering_title = 'o'
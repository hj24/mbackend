from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .models import GoodsCategory
from .serializers import GoodsSerializer
from .serializers import GoodsCategorySerializer
from .utils.pagination import GoodsListPaginator
from .utils.filters import GoodsFilter, OrderingFilter


# Create your views here.

class GoodsListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    """
    商品列表页，分页、搜索、过滤、排序
    """
    pagination_class = GoodsListPaginator
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    # 搜索、过滤、排序
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc',)
    ordering_fields = ('sold_num', 'add_time',)

    # def get_queryset(self):
    #     price_min = self.request.query_params.get('price_min', 0)
    #     queryset = Goods.objects.all()
    #     if price_min:
    #         return queryset.filter(shop_price__gt=price_min)
    #     return queryset

class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    list:
        商品列表分类数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('add_time',)
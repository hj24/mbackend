from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .serializers import GoodsSerializer
from .utils.pagination import GoodsListPaginator
from .utils.filters import GoodsFilter

# Create your views here.

class GoodsListViewSet(ListModelMixin,
                       viewsets.GenericViewSet):
    """
    商品列表页
    """
    pagination_class = GoodsListPaginator
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter

    # def get_queryset(self):
    #     price_min = self.request.query_params.get('price_min', 0)
    #     queryset = Goods.objects.all()
    #     if price_min:
    #         return queryset.filter(shop_price__gt=price_min)
    #     return queryset
import json

from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import Goods

class GoodsListView(View):
    """
    商品列表API
    """
    def get(self, request):
        goods = Goods.objects.all()[:10]

        json_list = []

        # for good in goods:
        #     json_dic = {}
        #     json_dic['name'] = good.name
        #     json_dic['category'] = good.category.name
        #     json_dic['market_price'] = good.market_price
        #     json_list.append(json_dic)

        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)

        return JsonResponse(json_data, safe=False)

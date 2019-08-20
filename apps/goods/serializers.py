from rest_framework.serializers import ModelSerializer

from .models import (Goods, GoodsCategory, GoodsImage)


class GoodsCategorySerializer(ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(ModelSerializer):

    class Meta:
        model = Goods
        fields = ('name', 'click_num')

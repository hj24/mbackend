from rest_framework.serializers import ModelSerializer

from .models import (Goods, GoodsCategory, GoodsImage)


class GoodsCategorySerializer(ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(ModelSerializer):

    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'

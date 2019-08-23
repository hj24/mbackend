from rest_framework.serializers import ModelSerializer

from .models import (Goods, GoodsCategory, GoodsCategoryBrand)


class GoodsCategorySerializer3(ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(ModelSerializer):

    sub_cat = GoodsCategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer(ModelSerializer):

    sub_cat = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(ModelSerializer):

    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
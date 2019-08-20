from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.

class GoodsListView(APIView):

    def get(self, request):
        goods = Goods.objects.all()
        serializered = GoodsSerializer(goods, many=True)
        return Response(serializered.data)
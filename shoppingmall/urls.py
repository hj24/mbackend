"""shoppingmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import (url, include)
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

import xadmin
from goods.views import GoodsListViewSet
from goods.views import CategoryViewSet


from shoppingmall.settings import MEDIA_ROOT


routers = routers.DefaultRouter()
routers.register(r'goods', GoodsListViewSet, base_name='goods')
routers.register(r'categorys', CategoryViewSet, base_name='categorys')

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*$)', serve, {'document_root': MEDIA_ROOT}),

    # 登录
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 商品列表
    url(r'^', include(routers.urls)),

    # drf生成文档
    url(r'doc/', include_docs_urls(title='malldoc')),
]

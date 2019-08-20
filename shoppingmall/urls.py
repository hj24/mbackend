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
import xadmin
from django.views.static import serve
from goods.views import GoodsListView
from rest_framework.documentation import include_docs_urls

from shoppingmall.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*$)', serve, {'document_root': MEDIA_ROOT}),

    # 登录
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 商品列表
    url(r'goods/$', GoodsListView.as_view(), name='goods-list'),

    # drf生成文档
    url(r'doc/', include_docs_urls(title='malldoc')),
]

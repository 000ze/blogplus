"""test2 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app01 import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url,include
app_name="app01"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(('order.urls','order'), namespace='order')),
    path(r'', include(('app01.urls','app01'), namespace='app01')),
    # path('blog/index/', views.index),
    # url('^blog/([A-Z][a-z]+)/article/([0-9]+)/$', views.article_detail),
    # url('^blog/([A-Z][a-z]+)', views.home),
    # path('login/', views.login),
    # path('logout/', views.logout),
    # path('reg/', views.register),
    # path('pc-geetest/register', views.get_geetest),
    # path('is_exist/', views.is_exist),
    # path('admin/', admin.site.urls),

    # media相关的路由设置
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]

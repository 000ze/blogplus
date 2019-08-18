"""first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings
from django.urls import path


urlpatterns = [
    path('blog/index/', views.index),
    url('^blog/([A-Z][a-z]+)/article/([0-9]+)/$', views.article_detail),
    url('^blog/([A-Z][a-z]+)', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('reg/', views.register),
    path('pc-geetest/register', views.get_geetest),
    path('is_exist/', views.is_exist),
   
    # media相关的路由设置
    url('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

]

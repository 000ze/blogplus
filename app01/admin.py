from django.contrib import admin

# Register your models here.
from app01 import models


admin.site.register(models.UserInfo)
admin.site.register(models.Article)
admin.site.register(models.Blog)
admin.site.register(models.ArticleDetail)
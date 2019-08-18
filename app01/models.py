from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png")
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

class Blog(models.Model):
    """
    博客信息
    """
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32, unique=True,verbose_name="博客分类")  # 个人博客后缀
    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "博客信息"
        verbose_name_plural = verbose_name

class Article(models.Model):
    """
    文章
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=True,unique=True,verbose_name="文章标题")  # 文章标题
    create_time = models.DateTimeField(auto_now_add=True,null=True,unique=True,verbose_name="创建时间")  # 创建时间
    category = models.ManyToManyField(to="Blog", null=True, verbose_name="博客分类")
    content=models.OneToOneField(to="ArticleDetail", null=True,on_delete=models.CASCADE,verbose_name="文章内容",)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章信息"
        verbose_name_plural = verbose_name

class ArticleDetail(models.Model):
    """
    文章详情表
    """
    content = models.TextField()

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name
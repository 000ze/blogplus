from django import template
from app01 import models
from django.db.models import Count

register = template.Library()


@register.inclusion_tag("left_menu.html")
def get_left_menu(category):
    # article_list = models.Article.objects.filter(category=category)
    # 查询文章分类及对应的文章数
    # category_list = models.Blog.objects.filter(category=category).annotate(c=Count("article")).values( "c")
    # 查文章标签及对应的文章数
    # tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # # 按日期归档
    archive_list = models.Article.objects.filter(category=category).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("id")).values("archive_ym", "c")

    return {
        # "category_list" :category_list,
        # "tag_list": tag_list,
        "archive_list": archive_list
    }

 # 如何在一个脚本或文件中加载Django项目的配置文件和项目信息
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test2.settings")
    import django

    django.setup()

    from app01 import models
    # books = models.Merchant.objects.all()[0]
    # print(books)
    # ret = models.Merchant.objects.get(id=1)
    # print(ret)
    # ret = models.Merchant.objects.filter(id=1)[0]
    # print(ret)
    # ret = models.Merchant.objects.values()
    # print(ret)
    # ret = models.Merchant.objects.values_list()
    # print(ret)
    # ret = models.Merchant.objects.all().order_by('id')
    # print(ret)
    # ret = models.Merchant.objects.all().order_by('id').reverse()
    # print(ret)
    # ret = models.Merchant.objects.all().count()
    # print(ret)
    # ret = models.Merchant.objects.all().first()
    # print(ret)
    # ret = models.Merchant.objects.all().last()
    # print(ret)
    # ret = models.Merchant.objects.all().exists()
    # print(ret)
    # 单表查询的双下划线
    # ret=models.Merchant.objects.filter(id__gt=1,id__lt=4)
    # print(ret)
    # ret=models.Merchant.objects.exclude(id__in=[2,3])
    # print(ret)

    # 外键
    # 正向查询
    # product_obj=models.Product.objects.get(id=2)
    # print(product_obj.merchant.name)
    # print(type(product_obj.merchant.name))
    # ret=models.Product.objects.filter(id=2).values("merchant__name")
    # print(ret)
    # 反向查询
    # merchant_obj=models. Merchant.objects.last()
    # ret=merchant_obj.product_set.all()
    # print(ret)
    # ret=models. Merchant.objects.filter(id=1).values("product__title")
    # print(ret)

    # 多对多
    # add
    # user_obj=models.User.objects.get(id=2)    # 第二个用户
    # ret=product_obj.merchant.all()

    # ret=user_obj.product.all()
    # print(ret)

    # product_obj=models.Product.objects.get(id=3) # 向第二个用户添加产品列表对应id=3的产品
    # user_obj.product.add(product_obj)
    # 添加多个
    # product_objs=models.Product.objects.filter(id__gt=3)  # 向第二个用户添加产品列表对应id=3的产品
    # user_obj.product.add(*product_objs)
    # 通过产品id添加
    # user_obj.product.add(2)

    # remove
    # 把id为2用户对应产品title="1223"的记录删除
    # product_objs = models.Product.objects.get(title="1223")
    # user_obj.product.remove(product_objs)
    # 把id为2用户对应产品id是2的记录删除
    # user_obj.product.remove(2)

    # clear
    # 将第二个用户对应的产品名全部删除
    # user_obj = models.User.objects.get(id=2)
    # user_obj.product.clear()

    # 外键的反向操作
    # product_objs = models.Product.objects.get(id=1)
    # product_objs.merchant.clear()

    from django.db.models import Avg, Sum, Max, Min, Count

    # # 聚合
    # ret=models.Product.objects.all().aggregate(price_sum=Sum("price"))
    # print(ret)

    # 分组
    # 查询每一件产品用户个数
    # ret=models.Product.objects.all().annotate(product_user=Count("user"))
    # for product in ret:
    #     print("产品：{}，用户数量：{}".format(product.title,product.product_user))

    # 查询用户个数大于1的产品
    # ret = models.Product.objects.all().annotate(product_user=Count("user")).filter(product_user__gt=1)
    # print(ret)

    # 查询各个用户对应产品的总价格
    # all_price = models.User.objects.all().annotate(price_sum=Sum("product__price")).values_list("price_sum")
    # ret = models.User.objects.all().annotate(price_sum=Sum("product__price"))
    # print(ret)
    # for i in ret:
    #     print(i,i.name,i.price_sum)
    # print(ret.values_list("id","name","price_sum"))

    # ret = models.User.objects.get(name="你好")
    # print(ret.id)

    # 在所有用户名后加上zx
    # from django.db.models import F ,Value
    # from django.db.models.functions import Concat
    # models.User.objects.update(name=Concat(F("name"),Value("zx")))

    # article_obj = models.Article.objects.values("category")
    # category= article_obj.Blog.all()
    # for i in article_obj:
    # print( article_obj)

    # article_list = models.Article.objects.all().order_by('id').reverse()
    # for i in article_list:
    #     print(i.title)
    #
    #     for x in  i.category.all():
    #         print(x)
    # ret=article_list.values_list("category")
    # for i in ret:

    # print(article_list)

    # 从文章得到对应的文章详情页
    # article_list = models.Article.objects.all()
    # for i in article_list:
    #     print(i.content)
    # article_list = models.Article.objects.all()
    # category=models.Blog.objects.get(id=2)
    # ret=article_list.category. all()
    # print(ret)

    # 从博客分类查询出相应的文章
    # ret = models.Blog.objects.all().annotate(category_article=Count("article"))[0]
    # category = models.Blog.objects.get(id=2)
    #     # article_list = models.Article.objects.filter(category=category)
    #     # print(article_list)
    # category = models.Blog.objects.get(id=2)
    # archive_list = models.Article.objects.filter(category=category).extra(
    #     select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    # ).values("archive_ym").annotate(c=Count("id")).values("archive_ym", "c")
    # category = models.Blog.objects.get(id=2)
    # archive_list = models.Article.objects.filter(category=category).extra(
    #     select={"c": "date_format(create_time,'%%Y-%%m')"}).values("c")
    # print(archive_list)
    # ret=models.Article.objects.all()
    # for i in ret:
    #     print(i.create_time)
    # category = models.Blog.objects.filter(category='Computer').first()


    # category='Computer'
    # category = models.Blog.objects.get(id=1)
    # print(type(category))
    # article_list = models.Article.objects.filter(category=category)
    # for i in article_list:
    #     print(i.content)

    category = models.Blog.objects.get(id=1)
    archive_list = models.Article.objects.filter(category=category).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("id")).values("archive_ym", "c")
    print(archive_list)
    for i in archive_list:
        print(i)

    # category = models.Blog.objects.get(id=1)
    # category_list = models.Blog.objects.filter(category=category).annotate(c=Count("article")).values("c")
    # for i in category_list:
    # #     print(i.content)
    #       print(i)
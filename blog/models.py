from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BlogArticles(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=None)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    # 定义排序规则 publish倒序 数据库表名blog_articles 管理后台显示blog列表
    class Meta:
        db_table = 'blog_list'
        ordering = ('-publish',)
        verbose_name_plural = 'blog列表'

    # 定义管理后台显示的字段
    def __str__(self):
        return self.title
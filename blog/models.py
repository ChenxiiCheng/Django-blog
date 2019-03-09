# coding: utf-8
import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要
    excerpt = models.CharField(max_length=200, blank=True, null=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    # 阅读量
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            # 首先实例化一个Markdown类，用于渲染body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将Markdown文本渲染成HTML文本
            # strip_tags 去掉HTML文本的全部HTML标签
            # 从文本摘取前54个字符赋给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        # 调用父类的save方法将数据保存刀数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'title']





from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


# Create your views here.

def blog_title(requests):
    blogs = BlogArticles.objects.all()
    return render(requests, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})

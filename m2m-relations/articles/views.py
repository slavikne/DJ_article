from django.shortcuts import render

from .models import Article, TagsArticle


def articles_list(request):
    object_list = Article.objects.all().prefetch_related('tags').all()
    # scopes = TagsArticle.objects.
    template = 'articles/news.html'
    context = {'object_list': object_list}
    print(object_list)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)

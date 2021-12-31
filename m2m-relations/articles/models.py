from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=256, verbose_name='Тематика')
    articles = models.ManyToManyField(
        Article,
        through='TagsArticle',
        related_name='tag',
    )


    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class TagsArticle(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tags')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    is_main = models.BooleanField(verbose_name='Основной')
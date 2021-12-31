from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, TagsArticle


class TagArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] == True:
                i += 1
        if i > 1:
            raise ValidationError('Основным может быть только один раздел')
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagArticleInline(admin.TabularInline):
    model = TagsArticle
    formset = TagArticleInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

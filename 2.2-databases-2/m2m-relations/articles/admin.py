from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count == 0:
            raise ValidationError('Выберите основной раздел')
        if count >= 2:
            raise ValidationError('Должен быть только 1 основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Article.tags.through
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):

    extra = 1
    inlines = [ScopeInline,]
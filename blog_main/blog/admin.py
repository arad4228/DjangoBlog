from django.contrib import admin
# 현재 디렉토리의 하위 디렉토리인 model에서 Post객체를 import
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # 자동으로 생성함(poppulate)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag,TagAdmin)

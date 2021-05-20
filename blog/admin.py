from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user_id
        
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
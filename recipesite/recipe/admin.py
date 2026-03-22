from django.contrib import admin
from .models import Recipe, Profile

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'main_category', 'sub_category', 'created_at')
    list_filter = ('main_category', 'sub_category')
    search_fields = ('title', 'description')


admin.site.register(Profile)
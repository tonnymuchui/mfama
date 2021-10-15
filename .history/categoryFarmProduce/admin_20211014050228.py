from django.contrib import admin
from .models  import CategoryFarmProduce

class CategoryFarmProduce(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(CategoryFarmProduce, CategoryAdmin)
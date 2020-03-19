from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, ReviewStudio, Masters


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'time', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'time', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class ReviewStudioAdmin(admin.ModelAdmin):
    list_display = ('studio_review', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('school_review',)

admin.site.register(ReviewStudio, ReviewStudioAdmin)



class MastersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'photo',
                    'body', 'direction', 'position', 'created', 'active']
    list_filter = ['created', ]

admin.site.register(Masters, MastersAdmin)
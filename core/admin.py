from django.contrib import admin

# Register your models here.
from .models import Profile, Review

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('school_review', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('school_review',)

admin.site.register(Review, ReviewAdmin)
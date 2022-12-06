from django.contrib import admin
from .models import Reviews
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'body',
        'date_added',
    )


admin.site.register(Reviews, ReviewAdmin)

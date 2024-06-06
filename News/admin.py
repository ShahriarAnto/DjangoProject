from django.contrib import admin
from News.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ("news_title" , "news_des")

# Register your models here.

admin.site.register(News , NewsAdmin)

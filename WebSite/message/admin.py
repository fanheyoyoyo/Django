# -*- coding: utf-8 -*-
from django.contrib import admin
from message.models import BookInfo, HeroInfo, God


# Register your models here.
class HeroForBook(admin.TabularInline):
    model = HeroInfo


class ManageShow(admin.ModelAdmin):
    inlines = [HeroForBook]
    search_fields = ['bTitle']
    list_display = ['bTitle', 'bType', 'bAuthor', 'bComment', 'bPubDate']


admin.site.register(BookInfo, ManageShow)


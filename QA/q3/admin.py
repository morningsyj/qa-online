from django.contrib import admin
from models import User2, Image2, Answer2


class AnswerAdmin2(admin.ModelAdmin):
    list_display = ['id', 'user', 'score', 'index_1', 'index_2']
    search_fields = ['image__name']


# Register your models here.
admin.site.register(User2)
admin.site.register(Image2)
admin.site.register(Answer2, AnswerAdmin2)

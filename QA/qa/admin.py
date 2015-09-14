from django.contrib import admin
from models import User, Image, Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'score', 'index_1', 'index_2']
    search_fields = ['image__name']


# Register your models here.
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Answer, AnswerAdmin)
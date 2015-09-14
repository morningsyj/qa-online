from django.db import models

# Create your models here.


class User2(models.Model):
    code = models.CharField(unique=True, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    answer_number = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def get_next(self):
        return self.get_image(self.answer_number)

    def get_image(self, number):
        if number >= 340:
            return -1, -1
        tmp = number / 34
        index_1 = ((self.id - 1) * 10 + tmp) % 35
        index_2 = number % 34
        if index_2 >= index_1:
            index_2 += 1
        return index_1, index_2

class Image2(models.Model):
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self, index):
        return '/media/newImages/img' + str(index) + '.bmp'

    def __unicode__(self):
        return self.name


class Answer2(models.Model):
    user = models.ForeignKey(User2, editable=False)
    index_1 = models.IntegerField(editable=False)
    index_2 = models.IntegerField(editable=False)
    score = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return str(self.index_1) + " : " + str(self.index_2)

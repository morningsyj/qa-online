from django.db import models

# Create your models here.


class User(models.Model):
    code = models.CharField(unique=True, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    answer_number = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def get_next(self):
        return self.get_image(self.answer_number)

    def get_image(self, number):
        if number >= 120:
            return -1, -1, -1
        tmp = number / 10
        image_id = (tmp / 4 * 100) + ((self.id - 1) * 4 + tmp % 4) % 100 + 1
        # index_1_array = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        # index_2_array = [2, 3, 4, 5, 3, 4, 5, 4, 5, 5]
        index_1_array = [1, 5, 4, 2, 3, 4, 1, 5, 4, 2]
        index_2_array = [2, 3, 5, 3, 1, 3, 5, 2, 1, 4]
        return image_id, index_1_array[number % 10], index_2_array[number % 10]


class Image(models.Model):
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self, index):
        tmp = self.name
        return '/media/sample/' + tmp + '-' + str(index) + '.bmp'

    def __unicode__(self):
        return self.name


class Answer(models.Model):
    image = models.ForeignKey(Image, editable=False)
    user = models.ForeignKey(User, editable=False)
    index_1 = models.IntegerField(editable=False)
    index_2 = models.IntegerField(editable=False)
    score = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.image.name
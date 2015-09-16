from django.db import models

# Create your models here.


class User2(models.Model):
    code = models.CharField(unique=True, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    answer_number = models.IntegerField(default=0)

    def sb(self, *arg):
        f = open('q3/seq.txt', 'r')
        self.index_1 = map(int, f.readline().strip().split(' '))
        self.index_2 = map(int, f.readline().strip().split(' '))
        f.close()
        models.Model.__init__(self, arg)

    def __unicode__(self):
        return str(self.id)

    def get_next(self):
        return self.get_image(self.answer_number)

    def get_image(self, number):
        if number >= 150:
            return -1, -1
        index = (self.id - 1) * 150 + number
        f = open('q3/seq.txt', 'r')
        s_index_1 = map(int, f.readline().strip().split(' '))
        s_index_2 = map(int, f.readline().strip().split(' '))
        f.close()
        index_1 = s_index_1[index]
        index_2 = s_index_2[index]
        return index_1, index_2

def fn_gen(index):
    fn_content = ['i05', 'i10', 'i18', 'i19']
    fn_distort_type = ['01', '08', '10', '11', '17']
    fn_distort_degree = ['1', '2', '3', '4', '5']
    content = index / 26
    sub_index = index % 26
    if sub_index == 25:
        return 'ref_images/' + fn_content[content] + '.bmp'
    else:
        distort_type = sub_index / 5
        distort_degree = sub_index % 5
        return 'distorted_images/' + fn_content[content] + '/' + fn_content[content] + '_' + fn_distort_type[distort_type] + '_' + fn_distort_degree[distort_degree] + '.bmp'


class Image2(models.Model):
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_url(self, index):
        return '/media/img3/' + fn_gen(index)
        
    def __unicode__(self):
        return self.name


class Answer2(models.Model):
    user = models.ForeignKey(User2, editable=False)
    index_1 = models.IntegerField(editable=False)
    index_2 = models.IntegerField(editable=False)
    score = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return fn_gen(self.index_1) + " : " + fn_gen(self.index_2)

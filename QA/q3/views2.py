from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from models import Answer2, Image2, User2
import models



# Create your views here.
def index(request):
    return render(request, 'index2.html')


def check_user(request):
    code = request.GET['code']
    if User2.objects.filter(code=code).count() == 0:
        return HttpResponseBadRequest()
    return HttpResponse()

#def get_url(index):
#    return "media/newImages/img" + str(index) + ".bmp"
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

def get_url(index):
    return '/media/img3/' + fn_gen(index)

def get_next(request):
    user = User2.objects.get(code=request.GET['user_code'])
    first_index, second_index = user.get_next()
    if first_index < 0:
        return JsonResponse({"error_code": 101})
    get_url(first_index)
    dic = {
        "number": user.answer_number + 1,
        "first": {
            "index": first_index,
            "url": get_url(first_index),
        },
        "second": {
            "index": second_index,
            "url": get_url(second_index),
        },
    }
    return JsonResponse(dic)


def create_answer(request):
    user = User2.objects.get(code=request.POST['user_code'])

    a = Answer2()
    a.user = user
    a.index_1 = request.POST['index_1']
    a.index_2 = request.POST['index_2']
    a.score = request.POST['score']
    a.save()

    user.answer_number += 1
    user.save()

    return HttpResponse()

def get_data(request):
    ans = Answer2.objects.order_by('id')
    res = HttpResponse(content_type='text/plain')
    res['Content-Disposition'] = 'attachment; filename="data.txt"'
    for i in ans:
        res.write(str(i.user.id) + ' ' + models.fn_gen(i.index_1) + ' ' + models.fn_gen(i.index_2) + ' ' + str(i.score) + '\n')
    
    return res

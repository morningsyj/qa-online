from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from models import Answer2, Image2, User2



# Create your views here.
def index(request):
    return render(request, 'index2.html')


def check_user(request):
    code = request.GET['code']
    if User2.objects.filter(code=code).count() == 0:
        return HttpResponseBadRequest()
    return HttpResponse()

def get_url(index):
    return "media/newImages/img" + str(index) + ".bmp"

def get_next(request):
    user = User2.objects.get(code=request.GET['user_code'])
    first_index, second_index = user.get_next()
    if first_index < 0:
        return JsonResponse({"error_code": 101})
    image = Image2.objects.get(pk=first_index)
    dic = {
        "number": user.answer_number + 1,
        "first": {
            "index": first_index,
            "url": image.get_url(first_index),
        },
        "second": {
            "index": second_index,
            "url": image.get_url(second_index),
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
        res.write(str(i.user.id) + ' ' + str(i.index_1) + ' ' + str(i.index_2) + ' ' + str(i.score) + '\n')
    
    return res

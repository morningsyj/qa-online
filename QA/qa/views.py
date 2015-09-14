from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from models import Answer, Image, User



# Create your views here.
def index(request):
    return render(request, 'index.html')


def check_user(request):
    code = request.GET['code']
    if User.objects.filter(code=code).count() == 0:
        return HttpResponseBadRequest()
    return HttpResponse()


def get_next(request):
    user = User.objects.get(code=request.GET['user_code'])
    image_id, first_index, second_index = user.get_next()
    if image_id < 0:
        return JsonResponse({"error_code": 101})
    image = Image.objects.get(pk=image_id)
    dic = {
        "id": image.id,
        "url": image.get_url(0),
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
    user = User.objects.get(code=request.POST['user_code'])
    image = Image.objects.get(pk=request.POST['image_id'])

    a = Answer()
    a.user = user
    a.image = image
    a.index_1 = request.POST['index_1']
    a.index_2 = request.POST['index_2']
    a.score = request.POST['score']
    a.save()

    user.answer_number += 1
    user.save()

    return HttpResponse()

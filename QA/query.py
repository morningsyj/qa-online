from qa.models import User
f = open("result.txt", "w")
x = User.objects.order_by("answer_number")
for i in x:
    if i.answer_number < 120:
        f.write(str(i.id) + " " + i.code + "\n")

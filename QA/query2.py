from qa.models import Answer
f = open("data.txt", "w")
for i in Answer.objects.order_by("image_id", "index_1", "index_2"):
    f.write(i.image.name + " " + str(i.index_1) + " " + str(i.index_2) + " " + str(i.score) + "\n")

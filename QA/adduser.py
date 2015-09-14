from q2.models import User2
for i in range(2, 100):
    u = User2()
    u.id = i
    u.code = str(i)
    u.answer_number = 0
    u.save()

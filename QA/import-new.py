import os
import django
from q2.models import Image2
django.setup()
files = os.listdir('./media/newImages')
for f in files:
    print(f)
    s = f[3:-4]
    print(s)
    if Image2.objects.filter(name=s).count() > 0:
        continue
    img = Image2()
    img.id = int(s)
    img.name = s
    img.save()

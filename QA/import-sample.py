import os
import django
from qa.models import Image
django.setup()
files = os.listdir('./media/sample')
for f in files:
    arr = f.split('-')
    iid = 0
    if arr[0] == 'W':
        iid = 100
    elif arr[0] == 'H':
        iid = 200
    iid += int(arr[1])

    if arr[2] != '0.bmp' or Image.objects.filter(name=arr[2]).count() > 0:
        continue
    img = Image()
    img.id = iid
    img.name = '-'.join(arr[0: 2])
    img.save()

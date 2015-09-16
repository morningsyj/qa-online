import random

n = 4
m = 26

s1 = []
s2 = []
idx = []

t = 0

for i in range(9):
    for j in range(n):
        for x in range(m):
            for y in range(x):
                index_1 = j * m + x
                index_2 = j * m + y
                if random.randrange(2) == 0:
                    index_1, index_2 = index_2, index_1
                s1.append(index_1)
                s2.append(index_2)
                idx.append(t)
                t = t + 1

random.shuffle(idx)

f = open('seq.txt', 'w')

for i in idx:
    f.write(str(s1[i]) + ' ')
f.write('\n')
for i in idx:
    f.write(str(s2[i]) + ' ')

f.close()

print t
#a미터 올라가고 b미터 내려가고 v미터가 목표
a, b, v = map(int, input().split())


day = int((v - b) / (a - b))

if (v - b) % (a - b) != 0 :
    print(day + 1)
else:
    print(day)


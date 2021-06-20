num = [None] * 5
sum = 0
avg = 0

for i in range(5) :
    num[i] = int(input())
    if num[i] < 40 :
        num[i] = 40
    sum += num[i]

avg = sum / 5
print(int(avg))
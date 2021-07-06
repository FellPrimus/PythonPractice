num = int(input())
count = 0

while num >= 0 :
    if num % 5 == 0:
        count = count + (num // 5)
        print(count)
        break
    num = num - 3
    count = count + 1
else:
    print(-1)
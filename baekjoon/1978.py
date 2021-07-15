num = int(input())
inputData = list(map(int, input().split()))
count = 0

for i in inputData:
    check = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            check += 1
    if check == 1 :
        count += 1


print(count)
inputData = int(input())

list = [0] * 2
sum = 0
count = 0

# 입력값 자리수 분할
list[0] = inputData // 10
list[1] = inputData % 10

#입력값과 합이 같을 때 while 탈출
while True :
    result = 0
    sum = list[0] + list[1]
    list[0] = list[1]
    list[1] = sum % 10
    result = list[0]*10 + list[1]
    count += 1
    if result == inputData:
        break


print(count)
num = int(input())

line = 1
sum = 1
while True:
    if num == 1:
        print('1')
        break
    sum += line * 6
    if num <= sum:
        print(line + 1)
        break
    else:
        line += 1
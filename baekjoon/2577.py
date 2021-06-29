num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 * num2 * num3

list = []
count = [0] * 10

for i in str(result):
    list.append(i)
    for j in range(0, 10):
        if int(i) == j:
          count[j]+=1
for i in count:
    print(i)
num = int(input())

inputData = [0] * num

for i in range(0, num):
    inputData[i] = int(input())

inputData = sorted(inputData)

for i in range(0, num):
    print(inputData[i])
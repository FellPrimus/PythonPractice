inputData = []
for i in range(9):
    inputData.append(int(input()))

m = max(inputData)
print(m)
index = inputData.index(m)
print(index+1)
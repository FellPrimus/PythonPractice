list = [0] * 10
count = 0
result = []

for i in range(0, 10):
    list[i] = int(input())
    result.append(list[i] % 42)

my_set = set(result)

for i in my_set:
    count += 1

print(count)
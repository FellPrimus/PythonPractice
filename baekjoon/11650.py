import sys
input = sys.stdin.readline

num = int(input())
array = []
for i in range(0, num):
    [x, y] = map(int, input().split())
    array.append([x, y])

sorted_array = sorted(array)

for i in range(0, num):
    print(sorted_array[i][0], sorted_array[i][1])

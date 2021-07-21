import sys

N = int(sys.stdin.readline())
list = [0] * N

for i in range(0, N):
    list[i] = int(sys.stdin.readline())

list.sort(reverse=True)

for i in range(N):
    list[i] = list[i] * (i + 1)

print(max(list))

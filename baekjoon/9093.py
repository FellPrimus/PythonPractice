T = int(input())

for i in range(T):
    arr = list(map(list, input().split()))
    for i in arr:
        print("".join(i[::-1]), end=" ")


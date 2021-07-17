n, k = map(int, input().split())


count = 0
sieve = [True] * (n + 1) #모든 수를 소수로 가정한다
for i in range(2, len(sieve) + 1):
    for j in range(i, n + 1, i):
        if sieve[j] == True:
            sieve[j] = False
            count += 1
            if count == k:
                print(j)
                break



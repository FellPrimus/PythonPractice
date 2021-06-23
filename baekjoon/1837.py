p, k = map(int, input().split())

def prime_number(n, check):
    for i in range(2, int(n**0.5) + 1):
        if check[i]:
            for j in range(i*2, n+1, i):
                if check[j]:
                    check[j] = False

check = [True] * (k+1)
check[0] = check[1] = False
prime_number(k, check)

for i in range(2, k):
    if check[i] and p % i == 0:
        print('BAD', i)
        exit()
print('GOOD')


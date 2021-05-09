counter = 0 #곱셈 나눗셈 합한 횟수
ptr = 0 #이미 찾은 소수의 개수
prime = [None] * 500

prime[ptr] = 2 #소수 2
ptr += 1

prime[ptr] = 3 #소수 3
ptr += 1

for n in range(5, 1001, 2) : #홀수일 때
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0: # %연산에서 나누어 떨어지므로 소수 아님을 판단
            break #소수가 아니므로 반복문 탈출
        i += 1
    else : #끝까지 나누어 떨어지지 않을 경우는 소수이다
        prime[ptr] = n #배열 소수에 등록
        ptr += 1
        counter += 1

for i in range(ptr) : #소수 배열을 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}') #연산 횟수 출력

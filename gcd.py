def gcd(x:int, y: int) -> int: #정수값 x, y의 최대 공약수 반환
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

if __name__ == '__main__':
    print('두 정수값의 최대 공약수를 구합니다')

    x = int(input('첫 번째 정수값 입력 : '))
    y = int(input('두 번째 정수값 입력 : '))

    print(f'두 정수값 최대 공약수는 {gcd(x,y)}')
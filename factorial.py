def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1) #0보다 크면 재귀호출하여 다시반복
    else:
        return 1

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값 입력 : '))
    print(f'{n}의 팩토리얼은 {factorial(n)}')
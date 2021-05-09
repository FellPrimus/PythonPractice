from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
            a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    print('배열 역순 정렬 ')
    nx = int(input('원소 수 입력 : '))
    x = [None] * nx #원소 수 nx인 리스트 생성

    for i in range(nx) :
        x[i] = int(input(f'x[{i}]값을 입력하십시오 : '))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬')
    for i in range(nx) :
        print(f'x[{i}] = {x[i]}')
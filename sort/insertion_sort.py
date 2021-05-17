from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

        for m in range(0, n - 1):  # 자리 교환 과정 표시
            print(f'{a[m]:2}', end='   ')
        print(f'{a[n - 1]:2}')

    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 했습니다')

if __name__ == '__main__':
    print('삽입 정렬 수행')
    num = int(input('원소 수를 입력 : '))
    x = [None] * num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
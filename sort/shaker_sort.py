from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right :
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last

if __name__ == '__main__':
    print('버블 정렬 수행')
    num = int(input('원소 수를 입력 : '))
    x = [None] * num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shaker_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
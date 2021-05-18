from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0 #검색 범위 맨 앞 인덱스
        pr = i - 1 #검색 범위 맨 뒤 인덱스

        while True:
            pc = (pl + pr) // 2 #검색 범위 가운데 인덱스
            if a[pc] == key: #검색 성공 : 인덱스와 키가 같다면
                break
            elif a[pc] < key: #인덱스가 키보다 작으면
                pl = pc + 1 #검색 범위 뒤쪽 절반으로 좁힘
            else: #인덱스가 키보다 크면
                pr = pc - 1 #검색 범위 앞쪽 절반으로 좁힘
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1 #삽입해야 할 위치 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == '__main__':
    print('이진 삽입 정렬 수행')
    num = int(input('원소 수를 입력 : '))
    x = [None] * num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


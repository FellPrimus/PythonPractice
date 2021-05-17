from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    ccnt = 0 #비교 횟수
    scnt = 0 #교환 횟수

    n = len(a)
    for i in range(n - 1):
        min = i # 최솟값 인덱스
        for j in range(i + 1, n) :
            if a[j] < a[min]:
                ccnt += 1 #비교하면 카운트
                min = j
        scnt += 1 #교환할때 카운트
        a[i], a[min] = a[min], a[i] # 맨 앞 원소와 자리 교환


        for m in range(0, n - 1): #자리 교환 과정 표시
            print(f'{a[m]:2}', end = '   ')
        print(f'{a[n - 1]:2}')

    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 했습니다')

if __name__ == '__main__':
    print('버블 정렬 수행')
    num = int(input('원소 수를 입력 : '))
    x = [None] * num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    selection_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
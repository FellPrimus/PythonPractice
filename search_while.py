from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True :
        if i == len(a):
            return -1 #검색에 실패하여 -1을 반환
        if a[i] == key:
            return i #검색에 성공하면 현재 검사한 인덱스(key)를 반환
        i += 1

if __name__ == '__main__':
    num = int(input('원소 수 입력 : ')) #num 값 입력받음
    x = [None] * num #원소 수 num인 배열 생성, None으로 채운다


    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력 : ')) #검색할 키 ky 입력받음

    idx = seq_search(x, ky) #ky와 같은 원소를 배열 x에서 검색하고 idx에 저장

    if idx == -1 :
        print('검색할 원소가 없습니다')
    else :
        print(f'검색 값의 위치는 x[{idx}] 입니다.')
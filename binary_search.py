from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int: #시퀀스 a에서 key와 일치하는 원소 이진 검색
    pl = 0 #검색 범위 맨 앞 원소 인덱스
    pr = len(a) -1 #검색 범위 맨 뒤 원소 인덱스

    while True :
        pc = (pl + pr) // 2 #중앙 원소 인덱스
        if a[pc] == key: #배열 pc번째 원소가 key와 같다면
            return pc #검색 성공 pc 리턴
        elif a[pc] < key:#배열 pc번째 원소가 key 보다 작으면
            pl = pc + 1 #검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1 #클 경우 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
        return -1 #검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력 : '))
    x = [None] * num #원소수 num인 배열 생성

    print('배열 데이터를 오름차순으로 입력')
    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]: #직전에 입력한 원소값보다 큰 값을 입력(오름차순)
                break

    ky = int(input('검색할 값 입력 : '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색 실패, 원소가 존재하지 않습니다')
    else :
        print(f'검색값은 배열 x[{idx}]에 위치합니다')

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int: #시퀀스 seq에서 key와 일치하는 원소를 보초법으로 검색
    a = copy.deepcopy(seq) #seq를 a로 깊은 복사
    a.append(key) #보초 key를 배열 마지막에 추가한다

    i = 0
    while True :
        if a[i] == key:
            break #key를 찾아 검색에 성공하면 while문 탈출
        i += 1 #없으면 배열 다음 항목 검색
    return -1 if i == len(seq) else i # i값이 seq의 길이와 같으면 배열 끝까지 검색한 것이므로 검색 실패한 것 -> -1 반환, 아니면 i를 반환하여 배열 위치를 특정한다

if __name__ == '__main__' :
    num = int(input('원소 수를 입력 : ')) #num 값 입력받음
    x = [None] * num #원소 수가 num 만큼인 배열 x 생성

    for i in range(num) :
        x[i] = int(input(f'x[{i}]: ')) #배열 x의 값들 입력받음

    ky = int(input('검색할 값을 입력 : ')) #검색할 값 ky 입력받음

    idx = seq_search(x, ky) #배열 x에서 ky와 같은 값 검색하여 idx에 저장

    if idx == -1:
        print('검색값을 찾을 수 없습니다')
    else:
        print(f'검색값은 x[{idx}]에 위치합니다')

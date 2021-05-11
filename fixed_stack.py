from typing import Any

class FixedStack: #고정 길이 스택 클래스
    class Empty(Exception): #비어 있을 경우 예외 처리
        pass

    class Full(Exception): #꽉 찼을 때 푸시하면 예외 처리
        pass

    def __init__(self, capacity: int = 256) -> None: #스택 초기화
        self.stk = [None] * capacity #스택 본체(배열)
        self.capacity = capacity #스택 크기 정의
        self.ptr = 0 #스택 포인터

    def __len__(self) -> int : #스택에 쌓여있는 데이터 개수 반환
        return self.ptr

    def is_empty(self) -> bool: #스택이 비어있는지의 여부 판단
        return self.ptr <= 0

    def is_full(self) -> bool: #스택이 꽉 차있는지의 여부 판단
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None: #스택에 데이터를 push
        if self.is_full(): #스택이 가득 차있는 경우를 먼저 체크
            raise FixedStack.Full
        self.stk[self.ptr] = value #포인터가 가리키는 배열의 위치에 저장 후
        self.ptr += 1 #포인터 위치를 하나 증가시킨다

    def pop(self) -> Any: #스택에서 데이터를 pop
        if self.is_empty(): #스택이 비어있는 경우를 먼저 체크
            raise FixedStack.Empty
        self.ptr -= 1 #포인터 위치를 하나 낮춘다.
        return self.stk[self.ptr]

    def peek(self) -> Any: #꼭대기 데이터를 체크
        if self.is_empty(): #스택이 비어 있을 경우
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None: #스택의 데이터를 모두 삭제
        self.ptr = 0 #포인터 초기화

    def find(self, value: Any) -> Any: #스택에서 값을 찾아 반환
        for i in range(self.ptr -1, -1, -1): #꼭대기부터 한단계씩 내려가며 검색
            if self.stk[i] == value:
                return i #검색 성공
        return -1 #실패

    def count(self, value: Any) -> bool: #저장된 데이터 수 반환
        c = 0
        for i in range(self.ptr): #바닥부터 올라가며 count
            if self.stk[i] == value: #검색 성공
                c += 1
        return c

    def __contains__(self, value: Any) -> bool: #스택에 값이 있는지 판단
        return self.count(value)

    def dump(self) -> None: #모든 데이터를 바닥부터 꼭대기까지 출력
        if self.is_empty():
            print('스택이 비어 있음')
        else:
            print(self.stk[:self.ptr])

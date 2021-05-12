from typing import Any

class FixedQueue: #고정 길이 큐 구현

    class Empty(Exception): #비어있는 큐에서 예외처리 필요할 때
        pass

    class Full(Exception): #꽉 차있는 큐에서 예외처리 필요할 때
        pass

    def __init__(self, capacity: int) -> None: #큐 초기화
        self.no = 0 #현제 데이터 개수
        self.front = 0 #맨 앞 원소 커서
        self.rear = 0 #맨 끝 원소 커서
        self.capacity = 0 #큐 크기
        self.que = [None] * capacity #큐 본체

    def __len__(self) -> int: #큐에 있는 모든 데이터 개수 반환
        return self.no

    def is_empty(self) -> bool: #큐가 비어 있는지 판단
        return self.no <= 0

    def is_full(self) -> bool: #큐가 꽉 차 있는지 판단
        return self.no >= self.capacity

    def enque(self, x:Any) -> None: #데이터 x를 큐 안에 넣음(인큐)
        if self.is_full():
            raise FixedQueue.Full #큐가 꽉 차면 예외처리
        self.que[self.rear] = x #맨 끝 커서에 위치한 큐 자리에 데이터 x 삽입
        self.rear += 1 #맨 끝 커서 rear를 한 칸 뒤로 옮긴다
        self.no += 1 #데이터 수를 하나 늘린다
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any: #데이터를 방출
        if self.is_empty():
            raise FixedQueue.Empty#큐가 비어 있으면 예외처리
        x = self.que[self.front] #맨 앞 커서에 위치한 데이터를 x로 꺼낸다
        self.front += 1 #데이터를 꺼냈으므로 맨 앞커서를 앞으로 땡긴다
        self.no -= 1 #데이터를 꺼냈으므로 수를 줄인다
        if self.front == self.capacity: #맨 앞 커서값이 큐 크기와 같다면 커서값을 초기화합니다
            self.front = 0
        return x

    def peek(self) -> Any: #맨 앞 데이터 체크
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front] #맨 앞 커서에 위치한 데이터 리턴

    def find(self, value: Any) -> Any: #값을 찾아 인덱스 반환
        for i in range(self.no) :
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value: #검색 성공
                return idx
        return -1 #실패

    def count(self, value: Any) -> bool: #큐 value 개수 반환
        c = 0
        for i in range(self.no): #큐 데이터 선형검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value: #검색 성공
                c += 1 #개수 카운터 올림
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None: #모든 데이터 삭제
        self.no = self.front = self.rear = 0 #큐의 데이터 모두 초기화

    def dump(self) -> None: #모든 데이터 출력
        if self.is_empty():
            print('큐가 비었습니다')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = '')
            print()





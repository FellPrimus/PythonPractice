from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data #데이터
        self.next = next #뒤쪽 포인터

class LinkedList:
    def __init__(self) -> None:
        self.no = 0 #노드 개수
        self.head = None #머리 노드
        self.current = None #주목 노드

    def __len__(self) -> int: #연결 리스트 노드 개수 반환
        return self.no

    def search(self, data: Any) -> int: #data와 값이 같은 노드 검색
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool: #연결 리스트에 data가 포함되어 있는지 확인
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None: #맨 앞에 노드삽입
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any): #맨 끝에 노드삽입
        if self.head is None:  #리스트가 비어 있을 때
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None: #꼬리 노드 찾는 과정, None 참조하면 종료
                ptr = ptr.next #맨앞부터 순서대로 스캔
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None: #맨 앞 노드 삭제
        if self.head is not None: #리스트가 비어 있을 때
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self): #맨 뒤 노드 삭제
        if self.head is not None:
            if self.head.next is None : #노드가 1개뿐일 때
                self.remove_first() #해당 노드를 삭제함
            else:
                ptr = self.head #스캔 중인 노드
                pre = self.head #스캔 중인 노드의 앞 노드

                while ptr.next is not None : #스캔 중인 노드의 다음이 비어있지 않으면
                    pre = ptr
                    ptr = ptr.next #자리를 옮긴다
                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head: #맨 앞 노드일 경우
                self.remove_first() #맨앞 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                    ptr.next = p.next
                    self.current = ptr
                    self.no -= 1

    def remove_current_node(self) -> None: #주목한 노드 삭제 함수
        self.remove(self.current)

    def clear(self) -> None: #전체 노드 삭제
        while self.head is not None:  #전체가 None 될 때 까지
            self.remove_first() #계속 앞 노드 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool: #주목 노드 한칸 뒤로
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print_current_node(self) -> None: #주목 노드 출력
        if self.current is None:
            print('주목 노드가 없습니다')
        else:
            print(self.current.data)

    def print(self) -> None: #모든 노드 출력
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)

class LinkedListIterator: #이터레이터용 클래스
    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.curretn is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


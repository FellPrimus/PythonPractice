from __future__ import annotations
from typing import Any, Type

class Node: #원형 이중 연결 리스트 노드 클래스
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev or self #앞쪽 포인터
        self.next = next or self #뒤쪽 포인터

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = self.current = Node() #더미 노ㅡㄷ 생성
        self.no = 0

    def __len__(self) -> int: #연결 리스트 노드 수 반환
        return self.no

    def is_empty(self) -> bool: #리스트 비었는지 확인
        return self.head.next is self.head

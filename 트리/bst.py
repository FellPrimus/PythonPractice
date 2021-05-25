from __future__ import annotations
from typing import Any, Type

class Node:#이진검색트리 노드
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None): #생성자
        self.key = key
        self.value = value
        self.left = left #왼쪽 포인터
        self.right = right #오른쪽 포인터

class BinarySearchTree:
    def __init__(self):#초기화
        self.root = None #루트

    def search(self, key: Any) -> Any: #키가 key인 노드 검색
        p = self.root #루트 주목
        while True:
            if p is None: #더 이상 진행할 수 없으면
                return None #값을 찾을 수 없음
            if key == p.key: #검색 성공
                return p.value
            elif key < p.key : #key가 더 작으면
                p = p.left #왼쪽 트리 검색
            else :
                p = p.right #key가 크면 오른쪽 트리 검색

    def add(self, key: Any, value: Any) -> bool: #키=key, 값=value 인 노드 삽입
        def add_node(node: Node, key: Any, value: Any) -> None:
            if key == node.key:
                return False #key가 이미 트리에 존재할 경우
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

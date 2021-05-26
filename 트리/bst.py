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

    def remove(self, key: Any) -> bool: #키가 key인 노드를 삭제
        p = self.root #스캔 중인 노드 주목
        parent = None #스캔 중인 노드의 부모 노드
        is_left_child = True

        while True:
            if p is None: #더 이상 진행할 수 없으면
                return False #그 키는 존재하지 않음

            if key == p.key: #key와 노드 p의 키가 같으면
                break #검색 성공
            else:
                parent = p #가지를 내려가기 전에 부모 설정
                if key < p.key: #key쪽이 작으면
                    is_left_child = True #왼쪽 자식으로 내려감
                    p = p.left #왼쪽 서브트리 검색
                else: #key 쪽이 클 경우
                    is_left_child = False #오른쪽 자식으로 내려감
                    p = p.right #오른쪽 서브트리 검색

        if p.left is None: #p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right #부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right #부모의 오른쪽 포인터 왼쪽 자식 가리킴
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left #부모 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left #부모 오른쪽 포인터가 왼쪽 자식 가리킴
        else:
            parent = p
            left = p.left #서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None: #가장 큰 노드 left 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key #left 키를 p로 이동
            p.value = left.value #left데이터 p로 이동
            if is_left_child:
                parent.left = left.left #left 삭제
            else:
                parent.right = left.left #left 삭제
        return True




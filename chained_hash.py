from __future__ import annotations
from typing import Any, Type
import hashlib

class Node: #해시를 구성하는 노드
    def __init__(self, key: Any, value: Any, next: Node) -> None :
        self.key = key # 키
        self.value = value  # 값
        self.next = next # 뒤쪽 노드 참조

class ChainedHash: #체인법으로 해시 클래스 구현
    def __init__(self, capacity: int) -> None :
        self.capacity = capacity #해시 테이블 크기 지정
        self.table = [None] * self.capacity #해시 테이블(리스트) capacity 크기만큼 생성

    def hash_value(self, key: Any) -> int: #해시값을 구하는 함수
        if isinstance(key, int) :
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any: #키가 key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key) #검색하는 키 해시값
        p = self.table[hash] #리스트에 해시값 순번의 값을 p에 저장

        while p is not None :
            if p.key == key:
                return p.value #노드 추가 성공
            p = p.next #뒤쪽 노드로 이동

        return None #검색 실패

    def add(self, key: Any, value: Any) -> bool: #키가 key이고 값이 value인 원소를 추가
        hash = self.hash_value(key) #추가하는 key의 해시값
        p = self.table[hash] #리스트에 해시값 순번의 값을 p에 저장

        while p is not None :
            if p.key == key:
                return False #노드 추가 실패
            p = p.next #뒤쪽 노드로 이동

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp #노드 추가
        return True #추가 성공

    def remove(self, key: Any) -> bool: #키가 key인 원소를 삭제
        hash = self.hash_value(key) #삭제할 key의 해시값
        p = self.table[hash] #리스트에 해시값 순번값 p에 저장
        pp = None #바로 앞의 노드 주목

        while p is not None :
            if p.key == key: #key를 발견하면?
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True #key 삭제 성공
            pp = pp
            p = p.next #뒤쪽 노드 주목
        return False #삭제 실패(key가 없을 경우)

    def dump(self) -> None: #해시 테이블 덤프
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None :
                print(f' -> {p.key} ({p.value})', end = '')
                p = p.next
            print()





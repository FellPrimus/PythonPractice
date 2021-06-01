from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입', '머리노드삭제', '꼬리노드삭제'
                     '주목노드출력', '주목노드이동', '주목노드역순이동', '주목노드삭제', '모든노드삭제'
                     '검색', '멤버십판단', '모든노드출력', '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList() #원형 이중 연결리스트 생성

while True:
    menu = select_Menu() #메뉴 선택

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값 입력 : ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드 넣을 값 입력 : ')))

    elif menu == Menu.주목노드바로뒤삽입:
        lst.add(int(input('주목 노드 바로 뒤 넣을 값 입력 : ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()
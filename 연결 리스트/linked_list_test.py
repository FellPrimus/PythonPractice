from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제', '꼬리노드삭제', '주목노드출력'
                     ,'주목노드이동', '주목노드삭제', '모든노드삭제', '검색', '멤버십판단', '모든노드출력'
                     ,'스캔', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList() #연결 리스트 생성

while True:
    menu = select_Menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값 입력 : ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값 입력 : ')))




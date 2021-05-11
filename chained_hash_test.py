from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료']) #메뉴 선언

def select_menu() -> Menu :
    #메뉴 선택
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end ='')
        n = int(input(': '))#메뉴 선택 입력받음
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13) #크기 13인 해시 테이블 생성

while True:
    menu = select_menu() #메뉴 선택

    if menu == Menu.추가 : #추가
        key = int(input('추가할 키 입력 : '))
        val = input('추가할 값 입력 : ')
        if not hash.add(key, val):
            print('추가를 실패했습니다.')

    elif menu == Menu.삭제 : #삭제
        key = int(input('삭제할 키 입력 : '))
        if not hash.remove(key):
            print('삭제를 실패했습니다.')

    elif menu == Menu.검색 : #검색
        key = int(input('검색할 키 입력 : '))
        t = hash.search(key)
        if t is not None :
            print(f'검색할 키를 갖는 값는 {t}')
        else :
            print('검색할 데이터가 없습니다.')
    elif menu == Menu.덤프 : #덤프
        hash.dump()
    else : #종료
        break

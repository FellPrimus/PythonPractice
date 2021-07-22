import sys
T = int(sys.stdin.readline())

for i in range(0, T):
    check = list(input())
    stack = list()
    is_empty = False
    for i in range(len(check)):
        if check[i] == '(':
            stack.append(check[i])
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty:
        print('YES')
    else:
        print('NO')
import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    inputData = sys.stdin.readline().split()

    if inputData[0]=='push':
        stack.append(inputData[1])
    elif inputData[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif inputData[0]=='size':
        print(len(stack))
    elif inputData[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif inputData[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
import sys
n = int(sys.stdin.readline())
inputData = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
MachingData = list(map(int, sys.stdin.readline().split()))

for i in MachingData:
    if i in inputData:
        print(1)
    else:
        print(0)


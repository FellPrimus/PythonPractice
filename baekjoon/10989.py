import sys
num = int(sys.stdin.readline())

inputData = [0] * 10001

for i in range(num):
    inputData[int(sys.stdin.readline())] += 1

for i in range(10001):
    sys.stdout.write('%s\n' % i * inputData[i])
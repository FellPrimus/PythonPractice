n = int(input())
score = []
count = 0

for _ in range(n):
    score.append(int(input()))

for i in range(n - 1, 0, -1):
    if score[i] <= score[i - 1]:
        count += (score[i - 1] - score[i] + 1)
        score[i - 1] = score[i] - 1

print(count)
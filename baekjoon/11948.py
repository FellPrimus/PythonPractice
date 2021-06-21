score = [None] * 6
sum = 0
for i in range(6):
    score[i] = int(input())

score1 = sorted(score[0:4], reverse=True)
for i in range(3):
    sum += score1[i]

if score[4] > score[5]:
    sum = sum + score[4]
else:
    sum = sum + score[5]

print(sum)
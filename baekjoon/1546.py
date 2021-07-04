subjectnum = int(input())
score = list(map(int, input().split()))
maxscore = max(score)
sum = 0

for i in range(0, subjectnum):
    score[i] = score[i] / maxscore*100
    sum += score[i]

avg = float(sum / subjectnum)

print(avg)

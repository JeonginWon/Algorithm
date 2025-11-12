N = int(input())
scores = list(map(int, (input().split())))

M = max(scores)
new_score=[]
for i in range(N):
    new_score.append((scores[i]/M)*100)
print(sum(new_score)/N)
def comb(count, idx):
    picked.append(temp[:])
    if count == n-1:
        return
    
    for i in range(1, n+1):
        if i > idx:
            temp.append(i)
            comb(count+1, i)
            temp.pop()

def bfs(a, group):
    visited[a] == 1
    que = [a]
    cnt = 0

    while que:
        x = que.pop(0)
        for i in node[x]:
            if visited[i] == 0 and i in group:
                visited[i] = 1
                que.append(i)
                cnt += 1
    return cnt


n = int(input())
population = [0] + list(map(int, input().split()))
node = [[_] for _ in range(n+1)]
for v in range(1, n+1):
    line = list(map(int, input().split()))
    for z in line[1:]:
        node[v].append(z)

temp = []
picked = []
comb(0,0)

ans = 1999999999

for pick in picked:
    not_pick = list(set([k for k in range(1,n+1)]) - set(pick))
    
    if len(pick) == 0 or len(not_pick) == 0:
        continue

    visited = [0]*(n+1)
    if bfs(pick[0],pick) + bfs(not_pick[0],not_pick) != n:
        continue

    area1 = 0
    area2 = 0

    for i in pick:
        area1 += population[i]

    for j in not_pick:
        area2 += population[j]

    if abs(area2-area1) < ans:
        ans = abs(area2-area1)

if ans == 1999999999:
    print(-1)
else:
    print(ans)
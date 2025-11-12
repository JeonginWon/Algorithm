from collections import deque                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

# 조합으로 노드 뽑기
def comb(count, idx):
    selected.append(temp[:])
    if count == n-1:
        return
    for i in range(1, n+1):
        if i> idx:
            temp.append(i)
            comb(count+1, i)
            temp.pop()
# bfs : 노드 조합마다 최솟값 갱신
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

# input
N = int(input()) #노드 수
population = [0] + list(map(int, input().split())) # 노드별 인구 수
node = [[_] for _ in range(N+1)]
# 인접한 노드 번호끼리 출력 (맨앞줄 노드 번호 , 그 뒤엔 그 노드와 인접한 노드들의 번호)
for n in range(1, N+1):
    line = list(map(int, input().split()))

    for z in line[1:]: # 인접한 구역의 번호
        node[n].append(z)


temp = []
selected = []
comb(0,0)
ans = 1999999999


for select in selected:
    not_select = list(set([k for k in range(1, n+1)]) - set(select))

    if len(select) == 0 or len(not_select) ==0:
        continue
    visited = [0] *(n+1)
    if bfs(select[0], select) + bfs(not_select[0], not_select) != n:
        continue

    area1 = 0
    area2 = 0
    for i in select:
        area1 += population[i]

    for j in not_select:
        area2 += population[j]

    if abs(area2-area1) < ans:
        ans = abs(area2-area1)

if ans == 1999999999:
    print(-1)
else:
    print(ans)
# 치킨 배달

# input
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
# 치킨집 좌표, 집 좌표 찾기
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        if city[i][j] == 2:
            chicken.append((i,j))


# 집에서 치킨집까지 최소 거리 계산하는 로직
def distance():
    total_dist = 0
    for hx, hy in house:
        dist = float("inf")
        for cx, cy in selected:
            dist = min(dist, abs(hx-cx) + abs(hy-cy))
        total_dist += dist
    return total_dist


# DFS로 치킨집 조합 선택
def dfs(start, cnt):
    global min_dis
    # 종료조건 : M개를 다 선택하면
    if cnt == M:
        min_dis = min(min_dis, distance()) #치킨거리 최솟값 출력
        return
    # 치킨집 하나씩 선택
    for i in range(start, len(chicken)):
        selected.append(chicken[i])
        dfs(i+1, cnt +1)
        selected.pop()

# 최소 거리 저장
min_dis = float("inf")
selected = [] # 치킨집 조합

dfs(0,0)
print(min_dis)
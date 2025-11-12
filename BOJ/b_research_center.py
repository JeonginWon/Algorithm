from copy import deepcopy
from collections import deque
# 연구소
# 안전영역 0의 갯수 최댓값구하기

# 빈칸의 3군데를 벽(1)로 만들기 - 벽세우기 함수
selected = []
def wall(start, cnt):
    global max_safe
    # 종료조건 : 벽 3개 다 세우면 return
    if cnt == 3:
        copy_center = deepcopy(center)
        # 벽세우기
        for x, y in selected:
            copy_center[x][y] = 1
        # case_count = len(blank)-3=0
        bfs_virus(copy_center) # 바이러스 퍼뜨리기
        safe_area = safe(copy_center) # 안정영역 계산
        max_safe = max(max_safe, safe_area) #최대 안전영역 갱신
        return
    
    for i in range(start, len(blank)):
        selected.append(blank[i])
        wall(i+1, cnt+1)
        selected.pop()

# 바이러스 확산 함수 BFS
def bfs_virus(matrix):
    q = deque(virus)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<= nx < N and 0<= ny <M and matrix[nx][ny] == 0: #빈칸에 바이러스 전파
                matrix[nx][ny] = 2
                q.append((nx, ny))

# 안전영역 계산 함수
def safe(matrix):
    safe_area = 0
    for n in range(N):
        for m in range(M):
            if matrix[n][m] == 0:
                safe_area += 1
    return safe_area


# input
N,M = map(int, input().split())
center = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 좌표 따로 저장
blank = []
virus = []
for i in range(N):
    for j in range(M):
        if center[i][j] == 0:
            blank.append((i,j))
        elif center[i][j] == 2:
            virus.append((i,j))
        
# 초기화
max_safe = 0
wall(0,0)
print(max_safe)


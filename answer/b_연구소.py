from collections import deque
from copy import deepcopy

# 벽 세우기 함수
selected = []
def wall(start, cnt):
    global max_safe_area
    # 종료 조건: 벽 3개 다 세우면
    if cnt == 3:
        # 연구소 복사본 생성
        copy_center = deepcopy(center)
        # 벽 세운 후 바이러스 확산
        spread_virus(copy_center)
        # 안전 영역 계산
        safe_area = calculate_safe_area(copy_center)
        # 최대 안전 영역 갱신
        max_safe_area = max(max_safe_area, safe_area)
        return
    
    for i in range(start, len(blank)):
        selected.append(blank[i])
        wall(i + 1, cnt + 1)  # 다음 빈칸으로 넘어감
        selected.pop()

# 바이러스 확산 함수 (BFS)
def spread_virus(lab):
    queue = deque(virus)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:  # 빈칸만 전파
                lab[nx][ny] = 2  # 바이러스가 퍼짐
                queue.append((nx, ny))

# 안전 영역 계산 함수
def calculate_safe_area(lab):
    safe_area = 0
    for i in range(N):
        for j in range(M):    
            if lab[i][j] == 0:  # 안전 영역은 빈 칸
                safe_area += 1
    return safe_area

# 입력 받기
N, M = map(int, input().split())
center = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸 좌표와 바이러스 좌표 따로 저장
blank = []
virus = []
for i in range(N):
    for j in range(M):
        if center[i][j] == 0:
            blank.append((i, j))
        elif center[i][j] == 2:
            virus.append((i, j))

# 최대 안전 영역 초기화
max_safe_area = 0

# 벽 세우기
wall(0, 0)

# 결과 출력
print(max_safe_area)

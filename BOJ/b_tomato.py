# 토마토
# BFS 실습

# 필요데이터
## 상자크기 M(가로)*N(세로)
## 토마토 상태 (1 : 익은 토마토, 0: 안익은 토마토, -1 : 토마토 없음)
## answer = 모든 토마토가 익는 최소 일수 (불가능 : -1, 처음부터 다 익었음 0)

# 1. 초기입력
# 토마토 상태를 2차원 배열에 저장함. 

# 2. 익은 토마토의 좌표를 알아야 함.
    # ㄱ. 익은 토마토의 좌표 저장 (값이 1인 좌표)
    # ㄴ. 좌표값들을 q 에 저장 (동시에 전파 시작)

# 3. 익은 토마토 좌표에서 동시다발적으로 전파하는 로직
    # ㄱ. 방향이 필요함 (델타)
    # ㄴ. 익은 토마토 좌표를 꺼내기 (반복)
            #> 4방향에 안익은 토마토 있으면 +1
            #> 새로 익은 토마토 좌표 갱신
            #> 새로 익은 토마토 좌표는 기존 좌표(값이 1) 에 +1 = 날짜 정보
                # 처음 익은 토마토 1, 다음날 익으면 2, 그 다음날 익은 건 3

# 4. 전파 끝나고 날짜 정보가 담긴 box완성
    # ㄱ. 0이 남아있으면 -> -1
    # ㄴ. 아니면 날짜 제일 큰 값 print 단, 1부터 시작하므로 answer = max -1

from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 토마토 좌표 저장
q = deque()
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            q.append((x, y))


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 전파 로직
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1  # box가 곧 날짜, 굳이 1로 저장할 필요가 없음. 누적값 활용
            q.append((nx, ny))

day = 0
for row in box:
    for val in row:
        if val == 0:  # 안 익은 토마토 남아있으면 -1
            print(-1)
            exit()
        day = max(day, val) # 아니면 day최댓값

print(day - 1)


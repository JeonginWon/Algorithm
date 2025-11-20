# 로봇청소기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# visited
visited = [[0] * M for _ in range(N)]
visited[r][c] = 1

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn_left(direction):
    return (direction - 1) % 4

cnt = 1
turn_time = 0

while True:
    d = turn_left(d)       # 방향 회전
    nr = r + dr[d]
    nc = c + dc[d]

    # 1) 왼쪽 방향이 아직 청소 안했고 벽이 아님
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        r, c = nr, nc
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 2) 네 방향 모두 청소 or 벽이면
    if turn_time == 4:
        # 후진: 방향 그대로에서 뒤로
        br = r - dr[d]
        bc = c - dc[d]

        # 후진 가능하다면 이동 (벽 아니면)
        if 0 <= br < N and 0 <= bc < M and room[br][bc] == 0:
            r, c = br, bc
            turn_time = 0
        else:
            break   # 후진도 불가능 → 종료

print(cnt)
# 벽 부수고 이동하기
# visited[x][y][wall] / wall : 벽 부쉈는지에 대한 여부

from collections import deque

def bfs(x,y,wall):
    # 덱 생성
    q = deque()
    q.append((0,0,0))
    #visited 생성
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    # delta
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y, wall= q.popleft()
        # 도착하면 거리 출력
        if x == N-1 and y == M-1:
            return visited[x][y][wall]
        # delta
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 다음칸으로 이동 가능, 아직 벽뿌x
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny][wall] and arr[nx][ny] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                q.append([nx,ny,wall])
            # 다음칸으로 이동 불가능, 벽뿌
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1 and wall == 0:
                visited[nx][ny][wall + 1] = visited[x][y][wall] +1
                q.append([nx,ny,wall+1])
    return -1


N,M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
print(bfs(0,0,0))


from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited = [[0]*M for _ in range(N)] # 방문한 좌표 표시할 2차원 행렬
    visited[x][y] = 0

    #delta
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]!=1 and miro[nx][ny]==1:
                visited[nx][ny] = visited[x][y]+1 #방문 표시 지나온 길에 +1
                q.append((nx, ny)) # 다음 진출 경로를 위해 현재좌표 q에 저장
    return visited

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)] 

answer = bfs(0,0)
print(answer[N-1][M-1])

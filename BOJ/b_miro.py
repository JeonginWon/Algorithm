from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and mirro[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited

N, M = map(int, input().split())
mirro = [list(map(int, input())) for _ in range(N)]  

answer = bfs(0, 0)   
print(answer[N-1][M-1])  

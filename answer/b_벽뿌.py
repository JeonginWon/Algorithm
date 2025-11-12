from collections import deque

def bfs():
    step = 1
    while q:
        for _ in range(len(q)):
            k, r, c = q.popleft()

            if r == N-1 and c == M-1:
                return step

            for dir in range(4):
                nk = k
                nr = r+dr[dir]
                nc = c+dc[dir]

                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue

                if graph[nr][nc] == 1:
                    if k == 1 or visited[1][nr][nc]:
                        continue
                    nk = 1
                else:
                    if visited[k][nr][nc]:
                        continue
                    nk = k
                visited[nk][nr][nc] = 1
                q.append((nk, nr, nc))

        step += 1
    
    return -1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]

q = deque()
visited[0][0][0] = 1
q.append((0, 0, 0))

print(bfs())
T = 10
def find_start(grid):
    for i in range(16):
        for j in range(16):
            if grid[i][j] == 2:
                return i, j
 
def find_end(grid):
    for i in range(16):
        for j in range(16):
            if grid[i][j] == 3:
                return i, j
 
def bfs(i, j):
    # visited 생성
    # 큐생성, 시작점 인큐
    # 인큐 표시
    visited = [[0] * 16 for _ in range(16)]
    q = [[i, j]]
    visited[i][j] = 1
 
    while q:
        ti, tj = q.pop(0)
        if grid[ti][tj] == 3:
            return 1
     
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti + di, tj + dj
            if 0<=wi<16 and 0<=wj<16 and grid[wi][wj] != 1 and visited[wi][wj] == 0: 
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
 
    return 0

for tc in range(1, T+1):
    input()
    grid = [list(map(int, input())) for _ in range(16)]
 
    start_i, start_j = find_start(grid)
    end_i, end_j = find_end(grid)
 
    print(f"#{tc} {bfs(start_i, start_j)}")
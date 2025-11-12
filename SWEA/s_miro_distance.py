# 미로의 거리

# visited 생성
# 큐생성, 시작점 인큐
# 인큐 표시
# 반복
# 		디큐
# 		방문해서 할 일
# 		방문 정점에 인접하고 미방문이면
# 				인큐
# 				인큐 표시

def find_start(N):
	for i in range(N):
		for j in range(N):
			if maze[i][j] == 2:
			    return i, j
def bfs(i, j, N):
	visited = [[0]* N for _ in range(N)]
	q = [[i,j]]
	visited[i][j] = 1
	while q:
		ti, tj = q.pop(0)
		if maze[ti][tj] == 3:
			return visited[ti][tj] -2
		for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
			wi, wj = ti+di, tj + dj
			if 0<= wi <N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
				q.append([wi,wj])
				visited[wi][wj] = visited[ti][tj] +1
				

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    if ans == None:
        print(f'#{tc+1} {0}')
    else:
        print(f'#{tc+1} {ans}')
		

from collections import deque
 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1
 
    s_r, s_c = -1, -1
    for r in range(N):
        temp = list(map(int, input()))
        for c in range(N):
            if temp[c] == 2:
                s_r, s_c = r, c
        graph.append(temp)
     
    q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[s_r][s_c] = 1
    q.append((s_r, s_c))
    flag = False
     
    while q:
 
        answer += 1
 
        for _ in range(len(q)):
            r, c = q.popleft()
     
            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]
 
                # 이 중 하나라도 만족하면 다음 방향을 보세요
                # 1. 맵 바깥쪽이거나
                # 2. 1이거나
                # 3. 방문했거나
                if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] == 1 or visited[nr][nc]:
                    continue
 
                if graph[nr][nc] == 3:
                    flag = True
                    break
 
                visited[nr][nc] = 1
                q.append((nr, nc))
             
            if flag:
                break
        if flag:
            break
     
    if not flag:
        answer = 0
 
    print(f'#{tc} {answer}')
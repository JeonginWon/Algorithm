# 해당 count 번째에서 구슬을 떨어뜨릴 행(+열)을 고르기

# 연쇄 폭발 영역을 탐색 > BFS

# 폭발 & 떨어뜨리기

# 함수
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
def crash(count, remain, graph):
    global answer
    # dfs니까 재귀함수 -> 탈출조건 필요
    if not remain or count == N:
        answer = min(answer, remain)
        return
    #1. 해당 count번째에서 구슬을 떨어뜨릴 행 고르기
    for i in range(W):
        # 해당 행이 비어있다면 스킵
        if not graph[i]:
            continue
        r = i
        c = len(graph[i]) - 1
        #2. 연쇄 폭발 영역 탐색 > BFS
        q= deque()
        visited = [[0]*H for _ in range(W)]

        next_remain -= 1
        visited[r][c] == 1
        q.append((r, c))

        while q:
            r,c = q.append
            if graph[r][c] == 1: # 1이면 연쇄폭발이 일어나지 않음
                continue
            for dir in range(4):
                for step in range(1, graph[r][c]):
                    nr = r+dr[dir]*step
                    nc = c+dc[dir]*step
                    # 맵 밖 벗어났을 때
                    if nr<0 or nr>=W or nc<0 or nc >= H:
                        continue
                    # 방문했을때
                    if visited[nr][nc]:
                        continue
                    # 해당 행의 사이즈를 벗어날 때
                    if len(graph[nr]) - 1 < nc:
                        continue
                    next_remain -=1
                    visited[nr][nc] = 1
                    q.append((nr, nc))

        #3. 폭파, 떨어뜨리기
        copy_graph = []
        for r in range(W):
            row = []
            for c in range(len(graph[r])):
                if visited[r][c]:
                    continue
                row.append(graph[r][c])
            copy_graph.append(row)
        crash(count+1, next_remain, copy_graph)


T = int(input())
for tc in range(T):
    N,W,H = map(int, input().split())
    input_graph = [list(map(int, input().split())) for _ in range(H)]

    graph =[]
    answer = 0

    for i in range(W):
        row = []
        for j in range(H):
            if input_graph[H-1-j][i] == 0:
                answer+= j
                break
            row.append(input_graph[H-1-j][i])
        else:
            answer += H
        graph.append(row)
    # 몇 번째 구슬
    # 남은 블럭 수 answer
    # 변화된 그래프 
    # -> 함수에서 이용

    # 
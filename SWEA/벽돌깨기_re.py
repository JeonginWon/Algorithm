# 벽돌깨기
# dfs, bfs, backtracking
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 구슬 개수(던지는 횟수카운트),남은 벽돌 갯수, 현재 벽돌 배열
def shoot(cnt, remains, now_arr):
    global min_blocks
    # 종료조건
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains) # 남은 벽돌 갯수와 최솟값 비교해서 최솟값 갱신
        return
    
    # 한 줄씩 떨구기
    for col in range(W):
        copy_arr = [row[:]for row in now_arr]
        row = -1

        # 가장 위 벽돌탐색
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        if row == -1:
            continue #벽돌 없으면 skip

        q= deque([(row, col, copy_arr[row][col])])
        now_remains = remains -1
        copy_arr[row][col] = 0 # 구슬이 처음 만나는 벽돌 자리

        while q:
            r, c, p = q.popleft()
            for k in range(1, p):
                for i in range(4):
                    nr = r+(dy[i] *k)
                    nc = c+(dx[i] * k)

                    #범위 밖이면 skip
                    if nr <0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    #벽돌 없으면 skip
                    if copy_arr[nr][nc] == 0:
                        continue
                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc]= 0
                    now_remains -= 1 

        #빈 공간 메꾸기
        for c in range(W):
            idx = H-1
            for r in range(H -1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -=1
        shoot(cnt+1, now_remains, copy_arr)

T = int(input())
for tc in range(T):
    N,W,H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9  
    blocks = 0
    
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1
 
    shoot(0, blocks, arr)
    print(f'#{tc+1} {min_blocks}')

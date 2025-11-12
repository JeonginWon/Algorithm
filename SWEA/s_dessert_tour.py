

T = int(input())


# i, j (대각선) x, y(대각선 이동 후 좌표)
def dfs(i, j, x, y, order, cnt):
    global answer
    #가지치기
    if x < 0 or x >= N or y < 0 or y >= N:
        return
     
    if i == x and j == y:
        if order == 4:
            answer = max(answer, cnt)
            return
    # 이미 방문한 번호면 return
    else:
        if cafe[x][y] in path:
            return

    # 방문한 카페 숫자 append
    path.append(cafe[x][y])
 
    if order <= 1:
        dfs(i, j, x+1, y+1, 1, cnt+1)
 
    if 1 <= order <= 2:
        dfs(i, j, x+1, y-1, 2, cnt+1)
 
    if 2 <= order <= 3:
        dfs(i, j, x-1, y-1, 3, cnt+1)
 
    if 3 <= order <= 4:
        dfs(i, j, x-1, y+1, 4, cnt+1)
     
    path.pop()
 
 
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
 
    answer = -1
 
    for i in range(N):
        for j in range(N):
            path = []
            dfs(i, j, i, j, 0, 0)
     
    print(f"#{tc} {answer}")
#파리퇴치3
#+ 
def plus_spray(x,y):
    delta = [(-1,0), (0,-1), (1,0), (0,1)]
    total = arr[x][y] #각 좌표 합(누적)

    for dx, dy in delta:
        for i in range(1, M):
            arr_x,arr_y = x+dx*i, y+dy*i
            if 0 <= arr_x <N and 0<= arr_y <N:
                total += arr[arr_x][arr_y]
    return total

#x
def cross_spray(x,y):
    delta = [(1,1),(1,-1),(-1,1),(-1,-1)]
    total = arr[x][y] #각 좌표 합(누적)

    for dx, dy in delta:
        for i in range(1, M):
            arr_x,arr_y = x+dx*i, y+dy*i
            if 0<= arr_x<N and 0<= arr_y <N:
                total += arr[arr_x][arr_y]
    return total

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #answer : max
    answer = 0
    for i in range(N):
        for j in range(N):
            max_flies = max(plus_spray(i,j),cross_spray(i,j))
            if max_flies > answer:
                answer = max_flies


    print(f'#{tc+1} {answer}')
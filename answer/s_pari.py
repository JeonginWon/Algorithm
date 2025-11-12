T= int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    flies =[list(map(int, input().split())) for _ in range(N)]

    #파리 시작점
    for r in range(N-M+1):
        for c in range(N-M+1):
            temp_sum  =0
            for i in range(M):
                for j in range(M):
                    temp_sum += flies[r+i][c+j]
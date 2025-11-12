#어디에 단어가 들어갈 수 있을까? 버전 2
T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        recent_c = -1

        for c in range(N):
            if graph[r][c] == 0:
                if c - recent_c -1 == K:
                    answer += 1
                    recent_c = c
                recent_c = c
        if c - recent_c -1 == K:
            answer +=1
    for c in range(N):
        recent_r = -1

        for r in range(N):
            if graph[r][c] == 0:
                if r - recent_r -1 == K:
                    answer += 1
                    recent_r = r
                recent_r = r
        if c - recent_r -1 == K:
            answer +=1

# 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T+1):
    N,K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        count = 0
        for c in range(N):
            #행을 고를때마다 count
            #1일 때마다 count 누적
            if graph[r][c] ==1:
                count+=1
                continue
            if count == K:
                answer +=1
            
            count = 0 
        if count == K:
            answer +=1

    for c in range(N):
            count = 0
            for r in range(N):
                #행을 고를때마다 count
                #1일 때마다 count 누적
                if graph[r][c] ==1:
                    count+=1
                    continue
                if count == K:
                    answer +=1
                
                count = 0 
            if count == K:
                answer +=1



T = 10
for tc in range(1, T+1):
    N = int(input())
    graph = [input() for _ in range(8)]
    answer = 0 #회문의 갯수
    
    #시작점 탐색
    for i in range(8):
        for j in range(8-N+1):

            #회문의 반을 잘라서 서로 비교
            #행검사
            for k in range(N//2):
                if graph[i][j+k] != graph[i][j+N-1-k]: #시작점 j로부터 N-1 끝글자로 가서 k만큼 비교(절반)
                    break 
                else: #회문이다
                    answer += 1

                #열검사
                for k in range(N//2):
                    if graph[j+k][i] != graph[j+N-1-k][i]: #시작점 j로부터 N-1 끝글자로 가서 k만큼 비교(절반)
                        break 
                    else: #회문이다
                        answer += 1
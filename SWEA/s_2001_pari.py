#파리퇴치
T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer=0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_block = 0
            for a in range(i,i+M):
                for b in range(j,j+M):
                    sum_block+= matrix[a][b]
            answer = max(answer, sum_block)
    print(f'#{tc+1} {answer}')
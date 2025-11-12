# 회문
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer=''

    #row
    for i in range(N):
        for j in range(N-M+1):
            part = arr[i][j:j+M]
            if part[::] == part[::-1]:
                answer = ''.join(part[::])


    transport = zip(*arr)
    trans = [list(tp) for tp in transport]
    for i in range(N):
        for j in range(N-M+1):
            part = trans[i][j:j+M]
            if part[::] == part[::-1]:
                answer= ''.join(part[::])



    print(f'#{tc+1} {answer}')


# 원래 회문

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    # 행 탐색
    for r in range(N):
        for i in range(N-M+1):
            words = arr[r][i:i+M]
            if words == words[::-1]:
                print(f'#{t+1}', ''.join(words))

    # 열 탐색
    for r in range(N):
        for c in range(N-M+1):
            words = ''
            for j in range(M):
                words += arr[c+j][r]
            if words == words[::-1]:
                print(f'#{t+1} {words}')
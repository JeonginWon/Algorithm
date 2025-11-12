# 회문
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer=''
    print(arr)
    #row
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][::-1] == arr[i][::]:
                answer = ''.join(arr[i][::])


    transport = zip(*arr)
    trans = [list(tp) for tp in transport]
    for i in range(N):
        for j in range(N-M+1):
            if trans[i][::-1] == trans[i][::]:
                answer= ''.join(trans[i][::-1])



    print(f'#{tc+1} {answer}')


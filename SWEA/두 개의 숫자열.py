T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    total = -float('inf')

    if N <= M :
        short, long = N, M
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else:
        long, short = N, M
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))

    for i in range(long-short+1):
        temp = 0
        for N in range(short):
            temp += A[N] * B[i+N]
        if temp >= total:
            total = temp

    print(f"#{tc} {total}")

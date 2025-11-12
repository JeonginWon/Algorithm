# 돌 뒤집기 게임 2
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    stones = list(map(int,input().split()))
    for m in range(M):
        i, j = map(int,input().split())
        for j_c in range(1, j+1):
            if i - j_c -1 >= 0 and j_c -1+ i <N :
                if stones[i-j_c-1] == stones[i+j_c-1]:
                    stones[i-j_c-1] = -(stones[i-j_c-1] -1)
                    stones[i+j_c-1] = -(stones[i+j_c-1] -1)
    print(f'#{tc+1}', end=' ')
    print(*stones)


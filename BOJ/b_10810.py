N, M = map(int, (input().split()))
list = [0]*N
for _ in range(M):
    i,j,k = map(int, (input().split()))
    for indx in range(i-1, j):
        list[indx]=k
print(*list)
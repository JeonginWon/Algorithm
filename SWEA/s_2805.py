T = int(input())
for tc in range(1, T+1):

    N = int(input())
    total = 0
    for i in range(N):
        values = list(map(int, list(input())))
        center = N//2
        if i <= center:
            total += sum(values[:])




print(f'#{tc} {}')

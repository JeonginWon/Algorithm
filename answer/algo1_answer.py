def is_increase(arr):
    before =-101
    for i in range(len(arr)):
        if arr[i] > before:
            before = arr[i]
            continue
        else:
            return 1

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0

    K = N/M
    if N%M > 0:
        K+= 1
    for count in range(K):
        idx = count*M
        answer += is_increase(numbers[idx:idx+M])
    print(f'#{tc} {answer}')

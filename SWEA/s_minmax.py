T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = max(numbers)-min(numbers)
    print(f'#{tc+1} {answer}')
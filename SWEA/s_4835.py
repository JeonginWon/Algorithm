#구간합
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, (input().split()))
#     a_i = list(map(int, input().split()))
#     #a_i오름차순 정렬 
#     a_i.sort()
#     answer = sum(a_i[-M:])-sum(a_i[0:M])
#     print(f'#{tc} {answer}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, (input().split()))
    a_i = list(map(int, input().split()))
    sum_a_i = []
    for i in range(N-M+1):
        sum_a_i.append(sum(a_i[i:i+M]))
        answer = max(sum_a_i)-min(sum_a_i)
    print(f'#{tc} {answer}')



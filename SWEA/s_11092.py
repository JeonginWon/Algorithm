# T = int(input())
# for tc in range(T):
#     N = int(input())
#     a = list(map(int, input().split()))
#     if a.count(max(a))> 1 :
#         answer = (a.index(max(a))+a.count(max(a))-1)- a.index(min(a))
#     else:
#         answer =  a.index(max(a)) - a.index(min(a))
#     # print(answer)
#     if answer < 0:
#         answer = -answer
#     else:
#         answer = answer
#     print(f'#{tc+1} {answer}')
# 최댓값의 마지막 index가 무조건 그 갯수만큼 + 되는 것 아님.
# 오답

T = int(input())
for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    
    max_a = max(a)
    min_a = min(a)
    
    max_idx = len(a) - 1 - a[::-1].index(max_a) #max값이 마지막으로 등장하는 곳
    min_idx = a.index(min_a)
    
    answer = abs((max_idx + 1) - (min_idx + 1))
    
    print(f'#{tc+1} {answer}')


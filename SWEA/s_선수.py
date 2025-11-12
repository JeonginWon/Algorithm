# N K : 선수의 수 N 허용되는 실력차이 K
# 선수마다의 실력값 배열
# 하나의 팀에 포함될 수 있는 가장 많은 팀원의 수 = answer
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 숫자크기 순으로 정렬
    arr.sort()
    # 선수의 수를 count해서 answer로 더해줌.
    answer = 0
    for i in range(N):
        for j in range(i, N):
            pass


#답안
T=int(input())
for tc in range(T):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))

    answer = 1 # 선수 최소 1명이 팀에 포함 + 거기에 더해주는 방식
    
    stats.sort()
    for i in range(N-1): #비교선수(본인)제외
        temp = 1 #몇명의 팀원과 비교했는지 count할 변수 생성 temp
        for j in range(i+1, N): #본인 다음 사람과 비교
            if stats[j] - stats[i] >K: # 실력차가 K초과하여 넘어가면 비교 중단
                break
            #else:
            temp += 1 #j를 밀면서 민 횟수만큼 카운트
        answer = max(answer, temp)


#left, right
T=int(input())
for tc in range(T):
    N, K = map(int, input().split())
    stats = list(map(int, input().split()))

    answer = 1 # 선수 최소 1명이 팀에 포함 + 거기에 더해주는 방식
    
    stats.sort()
    left = 0
    right = 0
    while right <N:
        if stats[right]- stats[right] <= K:
            right += 1
            continue
        answer = max(answer, right-left+1)
        left += 1
        print(answer)

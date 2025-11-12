# 삼성에서 신입사원을 어학 점수 기준으로 3개 반(A, B, C) 으로 나눔
# T1 < T2

# A반: 점수가 T2보다 큰 사람
# B반: 점수가 T1 이상 T2 이하인 사람
# C반: 점수가 T1보다 작은 사람
# 단, 다음 조건을 만족해야 함

# 각 반의 인원수는 최소 K_min 최대 K_max 여야함
# K_MIN 최소 인원의 3배를 넘지 않고, K_MAX는 최대 인원의 3배 이하
# 가장 많은 반과 가장 적은 반의 인원수 차이 최소값 출력
# K_min K_max 조건을 만족할 수 없으면 -1을 출력

# 입력 N, K_min, K_max 가 주어지고
# 그 다음 줄에 점수가 주어진다.

#테케안넣음
N, Kmin, Kmax = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

ans = float('inf')
    
# 가능한 모든 T1, T2 탐색

for i in range(N):          
    for j in range(i, N):   
        T1, T2 = scores[i], scores[j]
        
        A = []
        B = []
        C = []
        for s in scores:
            if s < T1:
                C.append(s)
        for s in scores:
            if T1 <= s < T2:
                B.append(s)
        for s in scores:
            if s>T2:
                A.append(s)

        if Kmin <= len(A) <= Kmax and Kmin <= len(B) <= Kmax and Kmin <= len(C) <= Kmax:
            diff = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))
            ans = min(ans, diff)
if ans == float("inf"):
    print('-1')

else:
    print(ans)


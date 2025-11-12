# 스타트와 링크
# N명 축구 - 스타트팀과 링크팀으로 나눈다.
# 능력치 (S): i번 사람과 j번 사람이 같은 팀일 때 더해지는 능력치 (즉, Sij+Sji)
# 능력치 차이를 최소로 하여라

# 아이디어 - 필요 로직
    # 1. 팀원 뽑기 - nC_2 (조합)
    # 2. 능력치 차이 계산 (DFS, 팀 조합에서 완탐), 최솟값 갱신

team_lst = []
def nCr(n, ans, r) :
    if n == len(members):
        if len(ans) == r:
            team = [i for i in ans]
            team_lst.append(team)
        return
    ans.append(members[n])
    nCr(n+1, ans, r)
    ans.pop()
    nCr(n+1, ans, r)


# input
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]   # 0부터 N-1로 관리하는게 편리함

nCr(0, [], N//2) # 팀원뽑기(조합)
# print(team_lst)


# 팀원 조합마다 능력치 합 (ability)계산
answer = 1e9
for t in range(len(team_lst)//2):
    start = team_lst[t]
    link = team_lst[len(team_lst)-1-t]

    #스타트 팀 능력치, 링크 팀 능력치
    s_sum, l_sum = 0, 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            s_sum += S[start[i]][start[j]] + S[start[j]][start[i]]

    for i in range(N//2):
        for j in range(i+1, N//2):
            l_sum += S[link[i]][link[j]] + S[link[j]][link[i]]
    #능력치 차 min
    answer = min(answer, abs(s_sum - l_sum))

# 능력치 차이의 최솟값 출력
print(answer)

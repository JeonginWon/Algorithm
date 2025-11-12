# 준환이의 양팔저울
 
 
# 두 번째 풀이 (DFS)
import math
 
def dfs(count, left, right):
    global answer
 
    # 왼쪽 무게가 전체 무게의 절반이면 왼쪽, 오른쪽 어디 놔도 상관이 없음
    # 바로 2^(N)*(N!) 공식 때려버리기
    if left >= total_weight / 2:
        answer += 2**(N - count) * math.factorial(N - count)
        return
 
    if count == N:
        answer += 1
        return
     
    for i in range(N):
        if visited[i]:
            continue
 
        visited[i] = 1
        dfs(count + 1, left+weights[i], right)
        if right + weights[i] <= left:
            dfs(count + 1, left, right + weights[i])
        visited[i] = 0
 
 
T = int(input())
 
for tc in range(1, T+1):
     
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
    visited = [0]*N
 
    answer = 0
 
    dfs(0, 0, 0)
    print(f"#{tc} {answer}")








# 다른 방법 memoization
def dfs(count, diff):
    global visited
    # 탈출 조건
    if dp[visited].get(diff):
        return dp[visited][diff]
 
    if count == N:
        dp[visited][diff] = 1
        return dp[visited][diff]
    # 무게 추 고르기
    case_count = 0
    for i in range(N):
        if visited & (1<<i): #방문되었으면
            continue
        #방문안되었으면 방문처리
        visited |= (1<<i)
        case_count+=dfs(count+1, diff+weights[i])
        # 오른쪽에 놓는 경우
        if diff-weights[i] >= 0:
            case_count+=dfs(count+1, diff-weights[i])
        visited ^= (1 << i)

    dp[visited][diff] = case_count
    return case_count
        

T = int(input())
 
for tc in range(1, T+1):
     
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
 
    answer = 0
 
    # (1 <= N <= 9 문제에서 주어짐)
    dp = [{} for _ in range(2**9)]
    visited = 0
# 보호필름
# 약물의 최소 투여횟수 정리  

# 연속하는 특성값 찾는 함수 test
    # > 특성값이 다 K개씩 있으면, 0출력
    # > 특성값 연속으로 된거 K개 미만 이면, 약투입 로직

def test(film):
    for i in range(W):
        test_0 = 0
        test_1 = 0
        test_pass = False #기본값 : 불합
        for j in range(D):
            if film[j][i] == 0:
                test_0 += 1
                test_1 = 0
            else:
                test_0 = 0
                test_1 += 1
            if test_0 == K or test_1 == K:
                test_pass = True # 합격
                break
        if not test_pass:# 기본값(불합)이 아니면 = 합격
            return 0
    
    return 1


# 약 투입 함수 dfs                        
    # film 가로로 탐색 
    # 가로_copy만들어서 그 row에 약을 넣는 경우는 두가지
    ## 1. 전부 다 0으로 만드는 시약 & 전부 1로 만드는 시약 구현
    ## 2. 시약 넣는 횟수 count +1
    ## 3. 한 줄씩 순회하면서 copy, 약넣기 반복
        # 종료조건 : count = min이면 return
        # 가지치기 조건 : count > min_count 이면 더이상 볼 필요없음, return

def dfs(cnt, idx):
    global min_cnt

    # 가지치기
    if cnt >= min_cnt:
        return
    #종료조건
    if test(film):
        min_cnt = cnt
        return
    
    for i in range(idx, D):
        film_copy = film[i][:]

        film[i] = [0]*W
        dfs(cnt+1, i+1)

        film[i] = [1]*W
        dfs(cnt+1, i+1)

        film[i] = film_copy
        

#input
T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_cnt = float('inf')

    if test(film):
        print(f'#{tc+1} 0')
        continue
    dfs(0,0)
    print(f'#{tc+1} {min_cnt}')

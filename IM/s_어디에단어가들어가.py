# IM 기출 : 어디에 단어가 들어갈 수 있을 까
T = int(input())
for tc in range(T):
    N,K = map(int, input().split())
    words = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    
    # 행 row 순회
    # cnt = 0 여기에서 초기화하면 항상 0
    for i in range(N):
        cnt = 0 # 행에서 1의 갯수를 저장할 cnt 변수 선언
        for j in range(N):
            if words[i][j] == 1:
                cnt += 1 # 1 count
                continue #1을 찾아도 계속
            if cnt == K: # 1의 갯수가 K개가 되면 answer에 카운트
                answer += 1
            
            cnt = 0 # 행에서 K개의 1을 이미 찾고 answer+=1 한 후, 이어서 찾을 때, cnt 초기화하고 다시 세야함. (11101)
        if cnt == K:
            answer += 1


    # 열 col 순회
    for j in range(N): #i, j 위치만 바꾸기
        cnt = 0 
        for i in range(N):
            if words[i][j] == 1:
                cnt += 1
                continue 
            if cnt == K: 
                answer += 1
            
            cnt = 0 
        if cnt == K:
            answer += 1
    print(f'#{tc+1} {answer}')
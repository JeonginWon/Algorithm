# 스위치 조작
T = int(input())
for tc in range(T):
    N = int(input())
    lights_A = list(map(int, input().split()))
    lights_B = list(map(int, input().split()))

    # 거꾸로 A상태와 B상태를 비교. 상태가 다르면 i번까지 스위치 누름
    # B상태가 될때까지 누른 횟수 cnt에 저장
    cnt = 0
    # 거꾸로 비교(뒤-> 앞)
    for i in range(N):
        if lights_A[i] != lights_B[i]:
            #다른 위치 = i -> i번째 까지 스위치 상태전환 (i~N-1)
            for j in range(i, N):
                lights_A[j] = 1- lights_A[j]
            cnt += 1 #한번 스위치 눌렀으므로 count
            if lights_A == lights_B:
                break # B상태에 다다르면 break
    print(f'#{tc+1} {cnt}')

# 답안
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    current = A[:] # 현재상태
    cnt = 0

    for i in range(N):
        if current[i] != B[i]: # 현재 상태와 B의 상태가 다르다면
            for j in range(i, N): # i부터 끝까지 바꾼다
                current[j] = 1 - current[j]
            cnt += 1

    print(f'#{tc} {cnt}')
# 스위치 켜고 끄기
N = int(input()) # 스위치 수
state = list(map(int, input().split())) # 스위치 상태
M =int(input()) # 학생 수
for m in range(M):
    gen, num = map(int, input().split()) # 성별, 받은 숫자

    #남자
    if gen == 1:
        for i in range(0,N):
            if (i+1) % num == 0:
                state[i] = 1-state[i]

    #여자
    elif gen ==2:
        idx = num -1 #num 번호 스위치의 인덱스 정의
        left = right = idx
        #좌우 대칭 확인
        while 0<= left-1 and right +1 <N and state[left-1]==state[right+1]:
            # 대칭이면 다음 인덱스로 이동 및 대칭인지 확인 반복
            left -= 1
            right += 1
        #대칭 구간 스위치 상태 변경
        for i in range(left, right+1):
            state[i] = 1-state[i]

#출력 (20개씩 줄바꾸기)        
for i in range(N):
    print(state[i], end =' ')
    if (i+1) % 20 ==0:
        print()

#필요 데이터

# N : 스위치의 수
# switches : 스위치의 상태
# M : 명령의 수
# gender : 명령의 성별
# number : 명령의 번호
# l, r : 여자의 명령을 수행하는 경우, 좌측 인덱스와 우측 인덱스

#로직

# 1. N, switches, M 입력
# M 줄에 걸쳐서 명령을 입력받기 (for)
#   ㄱ. 남자일 때
#   - number 부터 배수에 대하여 상태를 스왑해주기

#   ㄴ. 여자일 때
#   - 가운데 먼저 변경
#   - 좌우 대칭(ㅣ 지점과 r 지점이 값이 같을 때)을 만족할 때까지 반복
#   a. 해당 지점의 값을 스왑
#   b. l, r 지점을 갱신

N = int(input())
switches = list(map(int, input().split()))
switches.insert(0,0)

M = int(input())
for _ in range(M):
    gender, number = map(int, input().split())

    if gender ==1:

        idx = 1
        while number*idx <= N:
            switches[number*idx] = (switches[number*idx]+1)%2
            idx += 1

    else:
        switches[number] = (switches[number]+1)%2
        l = number-1
        r = number +1
        while 1 <= l and r <= N and switches[l] == switches[r]:
            switches[l] = (switches[l]+1) %2
            switches[r] = (switches[r]+1)%2
            l -= 1
            r += 1
#20개씩 출력하기
i = 1
while i<=N:
    print(*switches[i:i+20])
    i+=20
for i in range(1, N+1):
    print(switches[i], end = ' ')
    if (i+1) % 20 ==0:
        print()

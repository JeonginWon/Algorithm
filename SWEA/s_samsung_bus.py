#삼성시 버스노선
#필요데이터
T = int(input())
for tc in range(T):
    N = int(input()) #노선 수
    bus = [list(map(int, input().split())) for _ in range(N)] #노선이 가는 정류장 번호 범위
    P = int(input())
    bus_stop = []
    for _ in range(P):
        Cj = int(input())
        bus_stop.append(Cj)
    
    #노선이 지나는 정류장 갯수 count해서 저장할 list
    cnt_lst = []
    for _ in range(P):
        cnt_lst.append(0)
    #A,B범위의 정류장 count
    for n in range(N):
        for p in range(P):
            A,B = bus[n][0] , bus[n][1]
            if A<= bus_stop[p] <=B:
                cnt_lst[p] +=1
    print(f'#{tc+1}',end=' ')
    print(*cnt_lst)
# DAT 자료구조 : 값을 인덱스로 출력하는 것
# 두 전구 12741
T = int(input())



# 답안
T = int(input())

for tc in range(1, T+1):
    A,B,C,D = map(int,input().split())

    x_dat = [0]*101
    y_dat = [0]*101

    for i in range(A+1, B+1):
        x_dat[i] = 1 # i 값을 인덱스로 썼다
    
    for i in range(C+1, D+1):
        y_dat[i] =1

    cnt = 0
    for i in range(101):
        if x_dat[i] == 1 and y_dat ==1: cnt+=1

    print(f'#{tc} {cnt}')

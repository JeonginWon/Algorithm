def scanner(x):
    if x==[0,0,0,1,1,0,1]:
        return 0
    elif x==[0,0,1,1,0,0,1]:
        return 1 
    elif x==[0,0,1,0,0,1,1]:
        return 2
    elif x==[0,1,1,1,1,0,1]:
        return 3
    elif x==[0,1,0,0,0,1,1]:
        return 4
    elif x==[0,1,1,0,0,0,1]:
        return 5
    elif x==[0,1,0,1,1,1,1]:
        return 6
    elif x==[0,1,1,1,0,1,1]:
        return 7
    elif x==[0,1,1,0,1,1,1]:
        return 8
    elif x==[0,0,0,1,0,1,1]:
        return 9
  
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    code=[list(map(int,input().strip()))for _ in range(n)]
    res=0
    for x in range(n):
        for y in range(m-1, 56, -1):
            if code[x][y]==1:
                idx_x=x
                idx_y=y-55
                break
    pwd=code[idx_x][idx_y:idx_y+56]
    scan=[0 for _ in range(8)]
    for x in range(8):
        temp=pwd[7*x:7*(x+1)]
        scan[x]=scanner(temp)
        if x%2==0:
            res+=scan[x]*3
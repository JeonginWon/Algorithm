T = int(input())
for tc in range(T):
    N = int(input())
    a = list(input())

    lst = []
    for n in range(N):
        a_ct = a.count(a[n])
        lst.append(a_ct)
        lst_max= max(lst)
        indx = lst.index(lst_max)
    
        if sum(lst)//N == 1:
            number = max(a)
        else:
            number = a[indx]
    print(f'#{tc+1} {number} {lst_max}')


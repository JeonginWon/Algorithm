N, M =map(int, (input().split()))
lst =[]
for n in range(N+1):
    lst.append(n)

for _ in range(M):
    i,j = map(int, (input().split()))
    sub_lst = lst[i:j+1]
    rev_sub_lst = sub_lst[::-1]
    lst[i:j+1] = rev_sub_lst

print(*lst[1:])

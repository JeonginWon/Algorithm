N,M = map(int,(input().split()))
list =[]
for n in range(N+1):
    list.append(n)
# print(list)
for _ in range(M):
    i, j=map(int, (input().split()))
    a = list[i]
    list[i] = list[j]
    list[j] = a
print(*list[1:])
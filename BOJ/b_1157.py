#단어공부
N = list(input())
lst = []
for n in N:
    cnt_n = N.count(n)
    lst.append(cnt_n)
print(lst)
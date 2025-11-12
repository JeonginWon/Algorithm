lst = []
for i in range(10):
    num = int(input())
    rem = num%42
    lst.append(rem)
rem_set = set(lst)
print(len(rem_set))

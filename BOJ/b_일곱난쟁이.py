# 난쟁이들 키의 합이 100
import random
lst = []
for _ in range(9):
    heights = int(input())
    lst.append(heights)

#리스트에서 7개 자연수 추출 (반복)
while True:
    sample = random.sample(lst,7)
    sum_lst = sum(sample)
    if sum_lst == 100:
        break
    else:
        continue
answer = sorted(sample)
for i in range(7):
    print(answer[i])
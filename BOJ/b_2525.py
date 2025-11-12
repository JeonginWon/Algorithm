# A, B = map(int, input().split()) #현재 시각
# C = int(input()) #요리하는데 필요한 시간 (분)

# if B+C<60:
#     print(A, B+C)
# elif A+((B+C)//60)>=24:
#     print(0+A+((B+C)//60)-24, abs(60-((C-((C//60)*60))+B )))
# else:
#     print(A+((B+C)//60), 60-((C-((C//60)*60))+B))

#오답
#////////////////////////////////
A, B = map(int, input().split())
C = int(input()) 

min = A*60+B+C
if (min//60) >=24:
    print((min//60)-24, min%60)
else:
    print(min//60, min%60)
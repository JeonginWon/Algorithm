#대각선 출력
print('#++++\n+#+++\n++#++\n+++#+\n++++#')


#답안
for i in range(5):
    temp = ["+"]*5
    temp[i] = "#"

    temp = "".join(temp) #string 의 내장함수 join / ""은 구분자
    print(temp)
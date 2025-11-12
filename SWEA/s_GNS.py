T = int(input())
for tc in range(T):
    t, N = list(input().split())
    N = int(N)
    words = input().split()

    wn = {'ZRO': 0, 'ONE' :1,'TWO':2, 'THR': 3, "FOR" :4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN': 9}
    nw = {0 :'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:"FIV", 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    
    #word->number
    word_to_num=[]
    for w in words:
        word_to_num.append(wn[w])
        word_to_num.sort()

    
    #number->word
    num_to_word =[]
    for n in word_to_num:
        num_to_word.append(nw[n])
    print(f'#{tc+1}')
    print(*num_to_word)

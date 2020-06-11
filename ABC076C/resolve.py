def resolve():
    '''
    code here
    '''
    Sd = input()
    T = input()

    r_Sd = Sd[::-1]
    r_T = T[::-1]

    for i in range(len(Sd)- len(T)):
        temp_words = r_Sd[i:i+len(T)]
        res = r_Sd[:i]
        for j in range(len(T)):
            if temp_words[j] == '?' or temp_words[j] == r_T[j]:
                res+=r_T[j]
            else:
                break
        else:
            res = res + r_Sd[i+len(T):]
            print(res.replace('?', 'a')[::-1])
            break
    else:
        print('UNRESTORABLE')


if __name__ == "__main__":
    resolve()

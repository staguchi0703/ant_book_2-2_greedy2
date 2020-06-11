def resolve():
    '''
    code here
    '''
    Sd = input()
    T = input()

    r_Sd = Sd[::-1]
    r_T = T[::-1]

    def chk(a, b):
        res = ''
        for j in range(len(b)):
            if a[j] == '?' or a[j] == b[j]:
                res += b[j]
            else:
                return False
        else:
            return res 

    if len(Sd) >= len(T):
        for i in range(len(Sd)- len(T)+1):
            temp_words = r_Sd[i:i+len(T)]
            res = r_Sd[:i]
            
            temp = chk(temp_words, r_T)
            if temp:
                res = res + temp + r_Sd[i+len(T):]                
                print(res.replace('?', 'a')[::-1])
                break
        else:
            print('UNRESTORABLE')
    else:
        print('UNRESTORABLE')

if __name__ == "__main__":
    resolve()

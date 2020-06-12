def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    S = input()
    S_sorted = ''.join(sorted(S))

    T = ''
    cnt = 0

    for i in range(N):
        if S[i] == S_sorted[i]:
            pass
        else:
            #ここでSを入れ替えすれば入れる
            cnt +=1            

        T += S_sorted[i] 

        if cnt > K:
            break

    print(T + S[i+1:])


if __name__ == "__main__":
    resolve()

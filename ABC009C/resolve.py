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
            index_i = S.rfind(S_sorted[i],i)
            # print(index_i+i)
            a = S[i]
            b = S[index_i+i]
            S = S[:i] + b + S[i+1:]
            S = S[:index_i+i] + a + S[index_i+i+1:]

            cnt +=2            

        T += S_sorted[i]
        # print(''.join(S))
        # print(''.join(S_sorted))
        # print(''.join(T))
        # print('---', cnt)
        if cnt >= K:
            break

    print(''.join(T + S[i+1:]))


if __name__ == "__main__":
    resolve()

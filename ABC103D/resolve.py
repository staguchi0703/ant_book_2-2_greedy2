def resolve():
    '''
    code here
    '''

    N, M = [int(item) for item in input().split()]
    bridges = [[int(item) for item in input().split()] for _ in range(M)]

    bridges = sorted(bridges, key=lambda x:x[1])
    res = 1

    prev = bridges[0][1]
    for a, b in bridges:
        if a >= prev:
            res +=1
            prev = b

    print(res)    



if __name__ == "__main__":
    resolve()

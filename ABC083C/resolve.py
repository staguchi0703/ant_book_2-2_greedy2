def resolve():
    '''
    code here
    '''
    X, Y = [int(item) for item in input().split()]
    cnt = 0

    while X <= Y:
        X *= 2
        cnt +=1

    print(cnt)



if __name__ == "__main__":
    resolve()



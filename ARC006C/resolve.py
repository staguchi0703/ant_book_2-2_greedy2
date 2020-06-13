def resolve():
    '''
    code here
    '''

    N = int(input())
    weights = [int(input()) for _ in range(N)]
    cnt = 0

    while len(weights) > 0:
        temp =  weights.pop(0)
        cnt +=1

        memo = []
        for i in weights[:]:
            if temp >= i:
                weights.remove(i) 
                temp = i

    print(cnt)

if __name__ == "__main__":
    resolve()



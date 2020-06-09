def resolve():
    '''
    code here
    '''
    N = int(input())

    deff = 1000 - N
    coins = [500, 100, 50, 10, 5, 1]
    cnt = 0

    while len(coins) > 0:
        temp = coins[0]

        if deff >= temp:
            deff -= temp
            cnt += 1
        else:
            coins.remove(temp)

    print(cnt)



if __name__ == "__main__":
    resolve()

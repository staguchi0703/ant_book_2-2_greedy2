def resolve():
    '''
    code here
    '''
    N = int(input())
    robots = [[int(item) for item in input().split()] for _ in range(N)]


    arm_body_arm = []

    for body, arm in robots:
        arm_body_arm.append([body - arm, body + arm])
    
    arm_body_arm = sorted(arm_body_arm, key=lambda x:x[1])

    res = 1
    prev = arm_body_arm[0][1]
    for start, end in arm_body_arm:
        if prev <= start:
            res += 1
            prev = end

    print(res)

if __name__ == "__main__":
    resolve()

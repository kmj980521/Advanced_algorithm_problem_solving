def solve(n,value,price):
    # index = 1, ....., n
    l_max = [0] * (n+2) # prefix max
    r_max = [0] * (n+2) # suffix max
    for i in range(1,n+1):
        l_max[i] = max(l_max[i - 1], abs(value[i] - price[i]))
        r_max[i] = max(r_max[i + 1], abs(value[i] - price[i]))
    for i in range(n,0,-1):
        r_max[i] = max(r_max[i+1],abs(value[i]-price[i]))
    ll_max = [0] * (n+2) # prefix max without item i
    rr_max = [0] * (n+2) # suffix max without item 1

    # if item i is not involved, one of three prices (i-1, i, i+1) can be out!
    for i in range(2,n+1):
        ll_max[i] = min(l_max[i-1],max(ll_max[i-1], abs(value[i-1]-price[i])))

    for i in range(n-1,0,-1):
        rr_max[i] = min(r_max[i + 1], max(rr_max[i + 1], abs(value[i + 1] - price[i])))

    score = [0] * (n+1)
    for i in range(1,n+1):
        score[i] = min(max(ll_max[i], r_max[i+1]), max(l_max[i-1], rr_max[i]))

    idx = 1
    for i in range(2,n+1):
        if score[i] < score[idx]:
            idx = i
    return value[idx]

n = int(input())
value = [0] + [int(x) for x in input().split()]
price = [0] + [int(x) for x in input().split()]
value.sort()
price.sort()
ans = solve(n,value,price)
print(ans)
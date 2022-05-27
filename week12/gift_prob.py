import math



n = int(input())
#n = 4
max_N = n+10
values = [0] + list(map(int, input().split()))
tags = [0] + list(map(int, input().split()))


values.sort() # 상품의 가치를 정렬
tags.sort() # 가격표를 정렬
values.append(0) # dp를 진행하기 위해 마지막에 0을 append
tags.append(0) # dp를 진행하기 위해 마지막에 0을 append


dp = [[0 for col in range(4)] for row in range(max_N)]
dp[0][0]=dp[0][1]=dp[n+1][2]=dp[n+1][3]=0 # 바닥조건 설정


# Prob1
for i in range(n,0,-1):
    dp[i][2] = max(dp[i + 1][2], abs(values[i] - tags[i]))
    dp[i][3] = min(max(dp[i + 1][2], abs(values[i] - tags[i])), max(dp[i + 1][3], abs(values[i] - tags[i - 1])))

pair=[math.inf, math.inf]

# Prob2
for i in range(1,n+1):
    dp[i][0] = max(dp[i - 1][0], abs(values[i] - tags[i]))
    dp[i][1] = min(max(dp[i - 1][0], abs(values[i] - tags[i])), max(dp[i - 1][1], abs(values[i] - tags[i + 1])))
    compare_a = [max(dp[i - 1][1], dp[i + 1][2]) , values[i]]
    if pair[0] > compare_a[0]:
        pair = compare_a
    elif pair[0] == compare_a[0]:
        if pair[1] > compare_a[1]:
            pair = compare_a
    compare_b = [max(dp[i - 1][0], dp[i + 1][3]), values[i]]
    if pair[0] > compare_b[0]:
        pair = compare_b
    elif pair[0] == compare_b[0]:
        if pair[1] > compare_b[1]:
            pair = compare_b
print(pair[1])

"""
해결 과정
1. 상품을 제외하지 않을 때, 최적의 경우는 상품의 가치 리스트 values와 가격표 리스트 tags를 오름차순으로 정렬한 후 1:1 매칭을 하는 것이다.
2. 그러나 이때 n개의 상품 중 1개를 제외해서 최적의 경우를 구하기 위해서는 
제외하는 상품을 기준으로 같은 위치에 존재하는 tag 또는, 그 이전 위치의 tag 값과 비교한 후 그 차이가 최소가 되는 경우를 구해주고, 자신보다 더 작은 value를 가졌던 상품들에 대해서도 같은 연산을 진행하게 된다.
3. 즉, 그대로 같은 인덱스에 존재하는 value-tag 쌍을 가져갈지, 그 이전 인덱스에 위치하는 tag와 쌍을 이룰지 for문을 거쳐 dp 테이블을 구성한다(#Prob1 주석을 달아놓았습니다.).
4. 그 후, 구해준 모든 경우의 수를 비교해주며 최적의 경우를 구해나간다.
"""

"""
수행시간 분석
1. values와 tags 리스트를 정렬하는 데에 걸리는 시간 O(nlogn)
2. 정렬 후 기존 상품의 tags와 연결했을 경우, 이전 인덱스에 존재하는 tags에 연결했을 때의 경우를 구하는 for문 O(n)
3. 그 후, 구해준 모든 경우의 수에서 최적의 경우를 구해나가는 for문은 처음 상품부터 n개의 상품 모두 판별을 하기 때문에 O(n)
4. 가장 시간이 오래 걸리는 경우는 values와 tags를 정렬하는 데에 걸리는 시간이기 때문에 전체적인 시간복잡도는 O(nlogn)이 될 것이다.
"""
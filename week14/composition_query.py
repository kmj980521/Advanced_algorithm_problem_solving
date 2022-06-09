import sys
input = sys.stdin.readline

logN = 14 # log2 10000은 약 13.2xx -> 14로 지정
n = int(input()) # n 입력
fn = [0] + list(map(int, input().split())) # n개의 f(x)
num_of_query = int(input()) # 쿼리 수

sparse_table = [[fn[i]] for i in range(n + 1)]
#print(sparse_table)
for j in range(1, logN + 1):
    for i in range(1, n + 1):
        sparse_table[i].append(sparse_table[sparse_table[i][j - 1]][j - 1])

# 2^k 꼴인 모든 i에 대해 fi(x)를 미리 구해놓는다

for _ in range(num_of_query): # q의 반복
    x,pow_count = map(int, input().split())
    for a in range(logN, -1, -1): #log pow_count만큼의 반복 
        if pow_count >= 1 << a:
            pow_count -= 1 << a
            x = sparse_table[x][a]
    print(x)
		
"""
해결 방법
1. Sparse_table 자료구조를 사용하여 n개의 x가 존재한다고 할 때 쿼리를 O(logn)만에 처리한다.
2. sparse_table[i][x] = fx^i(x)를 의미한다.
3. sparse_table[i-1][x]는 f(x)를 2^(i-1)번 합성한 값으로 이 값을 t라고 하였을 때 sparse_table[i][x]는 f(t)를 2^(i-1)번 합성한 값으로 표현할 수 있따.
4. 따라서 점화식은 sparse_table[0][x] = f(x) | sparse_table[i][x] = sparse_table[i-1][sparse_table[depth-1][x]]가 될 것이다.
"""
"""
수행시간 분석
1. n을 입력받고 2차원 리스트로 sparse_table을 구성하는 데에 걸리는 시간은 O(n)
2. 구간의 쿼리를 빠르게 수행할 수 있도록 logN만에 쿼리를 처리하고자 n개의 값에 대해 sparse_table을 구성하는 시간은 O(nlogn)
3. 각각의 쿼리를 수행하는 시간은 O(logn) 단, 쿼리의 수는 q. 즉, 총 쿼리를 진행하는 데에 걸리는 시간은 O(qlogn)
4. 2,3번의 경우를 더하면 O((n+q)logn)이 수행시간이다.
"""

def LSB(k):
    return k & (-k)


n = int(input())
p_list = list(map(int, input().split()))  # P 수열
q_list = list(map(int, input().split()))  # Q 수열
P = []  # P 수열에 대한 정보와 각각의 인덱스를 다시 tuple 형식으로
Q = []  # Q 수열에 대한 정보와 각각의 인덱스를 다시 tuple 형식으로

for i in range(n):
    P.append([p_list[i], i + 1])
    Q.append([q_list[i], i + 1])

maxP = max(P)[0]
maxQ = max(Q)[0]

p_fenwicktree = [set([]) for x in range(maxP + 1)]  # P에서 max 값을 찾고 +1만큼의 길이를 새로 선언 -> 특정 값이 저장된 것을 알기 위해 set을 사용
q_fenwicktree = [set([]) for x in range(maxQ + 1)]

for i in range(len(P)):
    k = P[i][0]  # 특정 값
    while k <= maxP:  # maxP만큼
        p_fenwicktree[k] = p_fenwicktree[k].union(set([P[i][1]]))  # fenwick tree를 가며 P에서 특정 값이 속한 위치에 값을 모두 업데이트 한다.
        k += LSB(k)

for i in range(len(Q)):
    k = Q[i][0]
    while k <= maxQ:
        q_fenwicktree[k] = q_fenwicktree[k].union(set([Q[i][1]]))  # fenwick tree를 가며 Q에서 특정 값이 속한 위치에 값을 모두 업데이트 한다.
        k += LSB(k)

ALL_set = set(list(x for x in range(1, n + 1)))

result = 0
for i in range(n):
    p_small = set([])
    p_k = P[i][0] - 1
    # 특정 값 P[i] 보다 작은 값 (-1)의 집합을 찾아가는 코드
    while p_k >= 1:
        p_small = p_small.union(p_fenwicktree[p_k])
        p_k -= LSB(p_k)
    # print(p_temp)
    # 특정 값 Q[i] 보다 작은 값 (-1)의 집합을 찾아가는 코드
    q_small = set([])
    q_k = Q[i][0] - 1
    while q_k >= 1:
        q_small = q_small.union(q_fenwicktree[q_k])
        q_k -= LSB(q_k)

    # 특정 값 P[i] 보다 큰 값을 찾아가는 코드
    p_big = ALL_set - p_small  # 전체에서 자기 자신보다 작은 인덱스들을 제외
    p_big = p_big - set([i + 1]) - p_fenwicktree[
        P[i][0]]  # 자기가 속한 인덱스를 제외(set[i+1]) 또한,  자기 값인 인덱스들을 제외시켜 자기와 중복된 값들을 삭제

    # 특정 값 Q[i] 보다 큰 값을 찾아가는 코드
    q_big = ALL_set - q_small
    q_big = q_big - set([i + 1]) - q_fenwicktree[Q[i][0]]
    # 최종적으로 특정 위치 i에 대해 (P[i]보다 작고 동시에 Q[i]보다 작은 수)  x  (P[i]보다 크고 동시에 Q[i]보다 큰 수)를 하면 답이 된다
    result += (len(p_small & q_small) * len(p_big & q_big))

print(result)
"""
해결 과정
1. P 수열과 Q 수열 각각 최대값을 만들고 그 값 + 1 만큼의 새로운 리스트를 만들었다. 이때, P와 Q의 원소는 (값,index) 튜플의 데이터를 가진다 
2. P,Q 수열 각각의 원소 값을 접근해 그 값의 index의 set에 해당 값을 계속 update 해나가서 fenwick tree를 P와 Q에 대해서 구현하기 때문에 총 2개(p_fenwicktree,q_fenwicktree)를 구현한다. 
3. P 수열과 Q 수열 각각에 대해 특정 값 -> P[i][0]에 대해서 이 값보다 작은 것(p_small)을 구하고 이것을 토대로 특정 값보다 큰 것(p_big)을 구해주고 Q도 마찬가지이다.
4. 예를 들어 Pi,Qi가 있다고 할 때, (Pi보다 작으며 동시에 Qi보다 작은 수) x (Pi보다 크며 동시에 Qi보다 큰 수)가 답이 된다. (단, 동시에 크거나 작은 수는 같은 인덱스에 위치한다고 생각)
"""

"""
수행시간 분석
1. 처음 p_list와 q_list를 입력 받고 이것을 각각 (원소값, 인덱스)로 만들어주는 for문 O(n)
2. p_fenwicktree를 위해 최대값을 찾기 위한 max연산, q_fenwicktree를 위해 최대값을 찾기 위한 max연산 O(n)
3. 위의 값을 토대로 각각 새로운 set을 가지는 리스트를 선언하는 시간 O(max(P)+max(Q))

4-1. P 수열에서 특정 값에 대해 작은 것들의 set을 구하는 과정은 logn(fenwick tree로 LSB를 구하며 접근하기 때문)
4-2. Q 수열에서 특정 값에 대해 작은 것들의 set을 구하는 과정은 logn(fenwick tree로 LSB를 구하며 접근하기 때문)
4-3. P 수열에서 특정 값에 대해 큰 값들을 구하는 것은 기존에 구한 set에서 차집합을 구해주면 되는데 이때 차집합은 최대 n개의 원소를 가질 수 있기 때문에 O(n)
4-4. Q 수열 또한 마찬가지. O(n)
4-5. 4-1~4의 과정이 n번 반복되므로 O(2nlogn) + O(2n^2)

5. 실제로 수행시간에 영향을 주는 것은 3번 연산인 O(max(P)+max(Q))이다. 만약 max(P)가 100만이면 100만의 시간이 걸리게 된다. 
6. 즉 수행시간은 O(n^2) + O(max(P)+max(Q))
"""
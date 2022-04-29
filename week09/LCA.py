from math import log2
import sys
sys.setrecursionlimit(10**5)

def dfs(graph, v,d): # 전위 순회
    visited[v] = True  # 방문 처리
    depth[v] = d
    if len(graph[v]) == 0:  # 리프노드일 때
        return 
    for j in graph[v]:  # 노드 탐색
        if not visited[j]:  # 방문하지 않았다면
            parent[j] = v
            dfs(graph, j,d+1)  # 깊이가 1증가한 자식 노드들을 탐색
# sparse table(dp table) 구하기
def make_sparse_table():
    for i in range(n + 1):
        dp[i][0] = parent[i]
    for j in range(1, logN):
        for i in range(1, n + 1):
            dp[i][j] = dp[dp[i][j - 1]][j - 1]

def calculate_queries():
    # LCA
    for ele in queries:
        a, b = ele[0], ele[1]
        # 더 깊이 있는 노드의 조상을 찾아감. 
        if depth[a] > depth[b]:
            a, b = b, a
        diff = depth[b] - depth[a]
        for i in range(logN):
            if diff & 1 << i:
                b = dp[b][i]
        # 깊이 맞추고, 그 값이 같을 경우 최소 공통 조상은 a
        if a == b:
            print(a)
            continue
        # 루트 노드에서 부터 내려오면서 그 값이 달라지는 순간 찾기
        for i in range(logN - 1, -1, -1):
            if dp[a][i] != dp[b][i]:
                a = dp[a][i]
                b = dp[b][i]
        print(dp[b][0])

def solve():
    dfs(graph, 1, 1)
    make_sparse_table()
    calculate_queries()
    
n,q = map(int,input().split())
graph = [[] for _ in range(n + 1)] # 그래프 정보
visited = [False] * (n + 1) # 방문 처리를 위한 리스트
queries = [] # 쿼리
logN = int(log2(n) + 1)
dp = [[0] * logN for _ in range(n + 1)]
# input graph
for i in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

# input queries
for query in range(q):
    queries.append(list(map(int,input().split())))

# bfs 알고리즘으로 각 노드의 부모노드 및 depth 확인
parent = [0] * (n + 1)
depth = [0] * (n + 1)		
	
solve()

"""
해결과정
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, Sparse Table을 만들 때 가능한 최대 노드의 갯수는 logn + 1이므로 logN이라는 벼수를 선언하고, 이를 이용해 만들 dp table 리스트, 각 노드의 부모 정보를 저장할 parent 리스트, 각 노드의 depth를 확인하기 위한 depth 리스트를 선언한다. 
2. n-1만큼의 입력을 받아 간선의 정보를 저장한다.
3. q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
4. 전위순회를 dfs를 진행하며 특정 노드의 depth와 부모 노드의 정보를 parent 리스트에 저장한다. 
5. dfs를 한 후 만들어진 parent 리스트를 이용해 dp table에 각 노드의 부모의 저장을 저장한 후, 이를 이용해 logN까지 dp 테이블을 채워나가며 Sparse Table을 만든다.
6. 만들어진 Sparse Table을 이용해 LCA 알고리즘을 수행한다. 
"""

"""
수행시간 분석
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 각종 리스트를 만드는 데에 걸리는 시간은 O(n) + O(q) 시간이 걸린다.
2. dfs로 전위순회를 하며 depth, parent 리스트들을 구하는 시간은 모든 노드만을 탐색하면 되기 떄문에 O(n) 시간이 걸린다.
3. dfs로 구한 parent 리스트를 이용해 Sparse Table을(dp 리스트) 구하는 시간은 n개의 노드에 대해서 각각 O(log n)개의 최소 값을 저장해야 하므로 O(nlogn) 시간이 걸린다.
4. 두 노드 번호를 받아 쿼리를 진행하는데, q개의 쿼리에 대해 최악의 경우에는 각 노드가 제일 차상위 노드까지 올라가야 하는 횟수 즉, tree의 높이 logn번 실행하기 때문에 쿼리에 대한 수행시간은 O(qlogn) 시간이 걸린다.
5. 위의 수행시간을 모두 더하고 간편화 하면 O(nlogn + qlogn)이 나오므로 수행시간은 O((n+q)logn) 이다.
"""
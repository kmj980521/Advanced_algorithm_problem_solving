import sys

sys.setrecursionlimit(10 ** 5)


def dfs_preorder(graph, v):  # 전위순회
    global pre_count
    visited[v] = True
    pre_count += 1
    preorderList[v] = pre_count
    for j in graph[v]:
        if not visited[j]:
            dfs_preorder(graph, j)


def dfs_postorder(graph, v):  # 후위순회
    global post_count
    for k in graph[v]:
        if not visited[k]:
            dfs_postorder(graph, k)
    visited[v] = True
    post_count += 1
    postorderList[v] = post_count


def is_ancestor(u, v):
    if u <= 0 or u > n or v <= 0 or v > n:
        return False
    elif u == v:
        return True
    else:
        if preorderList[u] < preorderList[v] and postorderList[u] > postorderList[v]:
            return True
        else:
            return False


def calculate_queries():
    result = 0
    for i in queries:
        if is_ancestor(i[0], i[1]):
            result += 1
    print(result)


def solve():
    global visited
    dfs_preorder(graph, 1)  # preorder 전위순회
    visited = [False] * (n + 1)  # 방문 처리를 위한 리스트
    dfs_postorder(graph, 1)  # postorder 후위순회
    calculate_queries()


n, q = map(int, input().split())
visited = [False] * (n + 1)  # 방문 처리를 위한 리스트
graph = [[] for _ in range(n + 1)]  # 그래프
queries = []  # 쿼리
# input graph
for i in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)

# input queries
for query in range(q):
    u, v = map(int, input().split())
    queries.append([u, v])

pre_count = 0
preorderList = [0 for _ in range(n + 1)]  # 특정 노드( 노드1번 = [1] )가 preorder를 진행하며 몇 번째에 방문했는지 기록

post_count = 0
postorderList = [0 for _ in range(n + 1)]  # 특정 노드( 노드1번 = [1] )가 postrder를 진행하며 몇 번째에 방문했는지 기록

solve()

"""
해결 과정
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트를 선언한다. 
2. n-1만큼의 입력을 받아 간선의 정보를 저장한다.
3. q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
4. 전위순회를 할 때 몇 번째로 방문했는지 저장할 변수인 pre_count와 특정 노드가 몇 번째로 방문을 했는지 값을 저장할 리스트 preorderList를 선언하고, 후위순회도 마찬가지로 post_count와 postorderList를 선언한다. 
5. dfs_preorder를 거치며 전위순회를 하고 dfs_postorder를 거치며 후위순회를 해 preorderList와 postorderList를 완성시킨다.
6. 그 후 쿼리에 대해서 각각의 리스트에 특정 노드의 번호(preorderList와 postorderList 인덱스 그대로 접근)에 대한 쿼리를 진행해 결과를 얻는다.
"""

"""
수행시간 분석
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, visited 리스트, graph, queries를 만드는 데에 걸리는 시간은 O(n) + O(q) 
2. 만들어진 그래프를 사용해 dfs_preorder와 dfs_postorder를 순회하는 시간은 각각 O(n)이므로 2O(n)
3. dfs를 하며 만들어진 리스트를 사용해 ancestor를 판별하는 쿼리는 리스트에 접근해 값만 비교하면 되는 경우이기 때문에 O(1)이지만 이 과정이 q번 반복되기 때문에 O(q)이다.
4. 위의 수행시간을 모두 더하면 3O(n) + 2O(q) 이다.
5. 간편화 하면 즉, 수행시간은 O(n) + O(q)가 될 것이다.
"""

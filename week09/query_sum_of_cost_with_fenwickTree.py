# LSB 구하기
def LSB(k):
    return k & (-k)

def query_subtree(node_number):
    # preorder를 순회하고, cost를 기준으로 만든 fenwick_tree에서 (자기 번호 + 자식 수)  -   (자기 번호 -1) = 자신만의 subtree

    # 현재 노드 번호가 preorderList에서 존재하는 위치 + 자식 수가 현재 찾으려는 노드 + 위로도 연결된 subtree의 합.
    all_of_subtree = nodes_location[node_number] + child_node_count[node_number]  # 자기 번호 + 자식 수
    # 현재 노드 번호가 preorderList에서 존재하는 위치 -1은 현재 찾으려는 노드 보다 위에 트리이므로 subtree에서 제외
    not_subtree = nodes_location[node_number] - 1
    sum = 0

    # 자신의 subtree와 상위의 subtree를 순회하며 값을 더해나감
    while all_of_subtree >= 1:
        sum += fenwick_tree_by_preorder_cost[all_of_subtree]
        all_of_subtree -= LSB(all_of_subtree)
    # 자신의 subtree를 제외한 상위의 부분들을 제외해가며 값을 빼줌
    while not_subtree >= 1:
        sum -= fenwick_tree_by_preorder_cost[not_subtree]
        not_subtree -= LSB(not_subtree)
    print(sum)

def query_update(node_number, update_cost):
    # 현재 노드 번호가 preorderList에서 존재하는 위치를 구해줌.
    # 그 노드 이후부터 LSB를 더해가며 fenwick_tree를 업데이트
    # 즉, 자기와 연관된 것들을 update
    node_loc = nodes_location[node_number]
    while node_loc <= n:
        fenwick_tree_by_preorder_cost[node_loc] += update_cost
        node_loc += LSB(node_loc)


# 전위순회
def dfs(graph, v):
    global pre_count
    node_count = 0  # 자식 수
    visited[v] = True  # 방문 처리
    pre_count += 1
    nodes_location[v]=pre_count  # 특정 노드의 방문 시간
    if len(graph[v]) == 0:  # 리프노드일 때
        preorder_cost.append(nodes_cost[v])  # 자기 코스트를 append
        return node_count  # 상위 노드의 자식 수 1개 추가, 그 값을 return
    preorder_cost.append(nodes_cost[v])  # 자기 코스트를 append

    for j in graph[v]:  # 노드 탐색
        if not visited[j]:  # 방문하지 않았다면
            child_node_num = dfs(graph, j) + 1  # 그 노드까지의 자식 수를 탐색하고, 방금 탐색한 노드(+1)를 자식 수로 더해줌
            node_count += child_node_num  # 자식 노드의 수
    child_node_count[v] += node_count  # 특정 노드(v)의 자식 수에 자기 하위 subtree에서 구할 수 있는 자식 수를 더해준다.
    return node_count


def make_fenwick_tree_by_cost():
    # 편의상 1번 노드는 인덱스 1로 들어가게 했기 때문.
    # n개의 노드를 사용해 fenwick_tree 생성
    for i in range(1, n + 1):
        k = i
        while k <= n:  # n까지
            fenwick_tree_by_preorder_cost[k] += preorder_cost[i]  # 값을 update
            k += LSB(k)

def calculate_queries():
    # 쿼리 진행
    for i in queries:
        if i[0] == 'subtree':  # subtree면 노드 번호를 넘겨줌
            query_subtree(node_number=int(i[1]))
        elif i[0] == 'update':  # update면 노드 번호와 cost를 넘겨줌
            query_update(node_number=int(i[1]), update_cost=int(i[2]))


def solve():
    dfs(graph, 1)
    make_fenwick_tree_by_cost()
    calculate_queries()


n, q = map(int, input().split())

nodes_cost = [0] + list(map(int, input().split())) # 노드들의 cost. 계산하기 쉽게 각각의 노드 번호를 인덱스 그대로 사용하게끔 생성

graph = [[] for _ in range(n + 1)] # 그래프
queries = [] # 쿼리
# input graph
for i in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)

# input queries
for query in range(q):
    queries.append(input().split(' '))

visited = [False] * (n + 1) # 방문 처리를 위한 리스트
child_node_count = [0 for _ in range(n + 1)]  # 노드의 자식 수. 계산하기 쉽게 각각의 노드 번호를 인덱스 그대로 사용하게끔 생성

nodes_location = [[] for _ in range(n + 1)]  # 어떤 노드가 preorderList에서 어느 위치에 있는지
pre_count = 0 # preorder를 하며 방문하는 시간을 기록하기 위한 변수
preorder_cost = [0] # preorder를 하며, 방문한 노드 순서대로 각각 노드의 cost 값이 들어가게 한다.

fenwick_tree_by_preorder_cost = [0 for x in range(n + 1)] # preorder cost를 기준으로 fenwick_tree 만들기



solve()

"""
해결 과정
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, 각 노드에 대해 자식수를 구할 child_node_count 리스트, 각 노드가 preorderList에 몇 번째에 위치하는지 값을 구할 수 있는 nodes_location 리스트, 방문 순서대로 cost를 저장할 preorder cost 리스트, preorder cost로 만들 fenwick 트리인 fenwick_tree_by_preorder_cost 리스트를 선언한다. 
2. n-1만큼의 입력을 받아 간선의 정보를 저장한다.
3. q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
4. dfs를 전위순회를 하며 특정 노드의 방문 시간(nodes_location)과 언제 방문을 했는지(preorder_cost) 자기 cost를 append 하고 dfs를 수행할 때 마다 자식 수(child_node_count)를 구한다.
5. dfs를 거치며 만들어지는 preorder_cost를 이용해 fenwick_tree(각각의 인덱스는 특정 노드 번호까지의 cost의 합을 fenwick_tree를 구현한 것)를 구현한다. 
6. 그 후 각각의 쿼리에 대해 진행한다.
6-1) update
		1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.
		2) 그 노드의 번호부터 fenwick_tree를 거치며 각각의 tree에 위치한 값에 update_cost를 더해주며 값을 업데이트 한다. 
6-2) subtree
		1) preorder를 순회하고, cost를 기준으로 만든 fenwick_tree에서 (특정 노드의 위치 + 자식 수) - (특정 노드의 위치 - 1)이 자신의 subtree이므로, 현재 노드 번호가 preorderList에서 존재하는 위치(nodes_location)와 특정 노드의 자식 수(node_number)를 구한 all_of_subtree(특정 노드까지의 subtree)를 구한다.
		2) 현재 노드 번호가 preorderList에서 존재하는 위치(nodes_location) - 1 번째 위치는 특정 노드의 상위에 있는 node들을 제거한 값인 not_subtree(특정 노드의 상위 subtree들)를 구한다.
		3) all_of_subtree에 대해 fenwick_tree에 쿼리를 날려 각각의 값을 더해주며 sum 변수를 구해준다.
		4) not_subtree에 대해 fenwick_tree에 쿼리를 날려 위에서 구한 sum 변수에서 각각의 값을 빼주고 결과를 출력한다.

"""

"""
수행시간 분석
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 각종 리스트를 만드는 데에 걸리는 시간은 O(n) + O(q) 
2. dfs로 전위순회를 하며 nodes_location, preorder_cost,child_node_count를 구하는 시간은 모든 노드만을 탐색하면 되기 떄문에 O(n) 시간이 걸린다.
3. 값 하나로 fenwick_tree로 만드는 시간은 O(logn)이지만 n개의 cost들이 저장된 preorder_cost로 fenwick_tree를 만들기 때문에 O(nlogn) 시간이 걸린다.
4. subtree 쿼리는 현재 노드까지의 fenwick_tree의 합과, 현재 노드 -1의 fenwick_tree를 구하기 떄문에 O(logn) 시간이 걸린다.
5. update 쿼리는 현재 노드부터 fenwick_tree의 끝까지 업데이트 하지만 fenwick_tree는 길이가 n이기 때문에 최대 O(logn) 시간이 걸린다.
6. subtree 쿼리와 update 쿼리는 q만큼 실행하므로 O(qlogn) 시간이 걸린다. 
7. 위의 수행시간을 모두 더하고 간편화 하면 O(nlogn + qlogn)이 나오므로 수행시간은 O((n+q)logn)이다.
"""


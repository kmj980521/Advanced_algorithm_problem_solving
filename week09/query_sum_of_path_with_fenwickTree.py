# LSB 구하기
def LSB(k):
    return k & (-k)

def query_sum(node_number):
    # fenwick tree에서
    node_loc = nodes_location[node_number]#특정 노드의 번호가 위치한 지점을 fenwick tree에서 찾는다.
    sum = 0
    while node_loc >= 1 : # fenwick tree 끝까지
        sum += fenwick_tree_by_dif[node_loc] # query_sum 진행 즉, 특정 노드 번호까지의 거리를 구해준다.
        node_loc-=LSB(node_loc)
    print(sum)

def query_update(node_number, update_cost):
    node_loc = nodes_location[node_number] # 특정 노드의 번호가 위치한 지점
    not_subtree = node_loc + child_node_count[node_number] + 1 # 특정 노드의 번호가 위치한 지점 + 자식 수 + 1 --> 특정 노드의 subtree 이외의 구간은 다시 값을 감소
    while node_loc <=n:
        fenwick_tree_by_dif[node_loc]+=update_cost # 특정 노드의 번호가 위치한 지점부터 fenwick tree 업데이트
        node_loc+=LSB(node_loc)
    while not_subtree <=  n: # 특정 노드의 subtree가 아닌 곳에 값을 다시 감소
        fenwick_tree_by_dif[not_subtree] -= update_cost
        not_subtree +=LSB(not_subtree)

def calculate_queries():
    # 쿼리 진행
    for i in queries:
        if i[0] == 'sum':  # subtree면 노드 번호를 넘겨줌
            query_sum(node_number=int(i[1]))
        elif i[0] == 'update':  # update면 노드 번호와 cost를 넘겨줌
            query_update(node_number=int(i[1]), update_cost=int(i[2]))

def dfs(graph, v,cost): # 전위 순회 
    global pre_count
    node_count = 0  # 자식 수
    visited[v] = True  # 방문 처리
    pre_count += 1
    nodes_location[v]= pre_count  # 특정 노드의 방문 시간

    preorderList.append(v)
    path_sum.append(cost) # 현재까지의 cost를 append (특정 노드의 방문이 이루어졌을 때 append가 일어난다)
    if len(graph[v]) == 0:  # 리프노드일 때
        return node_count  # 상위 노드의 자식 수 1개 추가, 그 값을 return
    for j in graph[v]:  # 노드 탐색
        if not visited[j]:  # 방문하지 않았다면
            child_node_num = dfs(graph, j,cost+nodes_cost[j]) + 1  # 그 노드까지의 자식 수를 탐색하고, 방금 탐색한 노드(+1)를 자식 수로 더해줌
            node_count += child_node_num  # 자식 노드의 수
    child_node_count[v] += node_count  # 특정 노드(v)의 자식 수에 자기 하위 subtree에서 구할 수 있는 자식 수를 더해준다.
    return node_count

def make_fenwick_tree_by_dif():
    # 편의상 1번 노드는 인덱스 1로 들어가게 했기 때문.
    # n개의 노드를 사용해 fenwick_tree 생성
    for i in range(1, n + 1):
        k = i
        while k <= n:  # n까지
            fenwick_tree_by_dif[k] += dif[i]  # 값을 update
            k += LSB(k)
# path_sum으로 dif 구해주기
def make_dif_list():
    dif[1] = path_sum[1]
    for i in range(2, n + 1):
        dif[i] = path_sum[i] - path_sum[i - 1]

def solve():
    dfs(graph, 1, nodes_cost[1]) # 1번 노드부터 dfs로 path_sum을 구함
    make_dif_list() # path_sum으로 dif 리스트 구하기
    make_fenwick_tree_by_dif() # dif로 fenwick tree 구하기
    calculate_queries() # 쿼리 진행

n, q = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 그래프
queries = [] # 쿼리
preorderList =[0]
visited = [False] * (n + 1) # 방문 처리를 위한 리스트
child_node_count = [0 for _ in range(n + 1)]  # 노드의 자식 수. 계산하기 쉽게 각각의 노드 번호를 인덱스 그대로 사용하게끔 생성
nodes_location = [[] for _ in range(n + 1)]  # 어떤 노드가 preorderList에서 어느 위치에 있는지
pre_count = 0 # preorder를 하며 방문하는 시간을 기록하기 위한 변수
path_sum = [0]  # 특정 노드까지의 거리. (preorder 순서대로 들어간다)
dif = [0 for _ in range(n + 1)]

nodes_cost = [0] + list(map(int, input().split())) # 노드들의 cost. 계산하기 쉽게 각각의 노드 번호를 인덱스 그대로 사용하게끔 생성

# input graph
for i in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)

# input queries
for query in range(q):
    queries.append(input().split(' '))

fenwick_tree_by_dif = [0 for x in range(n + 1)] # preorder cost를 기준으로 fenwick_tree 만들기

solve()



"""
해결 과정
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, 각 노드에 대해 자식수를 구할 child_node_count 리스트, 각 노드가 preorderList에 몇 번째에 위치하는지 값을 구할 수 있는 nodes_location 리스트, preorder dfs를 하며 방문하는 순서대로 노드의 cost를 저장할 path_sum 리스트, path_sum 리스트를 이용해 인접한 값의 차이를 저장할 dif 리스트, preorder cost로 만들 fenwick 트리인 fenwick_tree_by_dif 리스트를 선언한다. 
2. n-1만큼의 입력을 받아 간선의 정보를 저장한다.
3. q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
4. dfs를 전위순회를 하며 특정 노드의 방문 시간(nodes_location)과 언제 방문을 했는지 preorderList에 append를 해주고 해당 노드의 cost를 path_sum리스트에 append하고, dfs를 수행할 때 마다 자식 수(child_node_count)를 구한다.
5. 그 후 구한 path_sum 리스트를 이용해 인접한 값의 차이를 저장하는 dif 리스트를 만든다.
6. dif 리스트를 이용해 fenwick_tree_by_dif라는 fenwick_tree를 만든다.
7. 그 후 각각의 쿼리에 대해 진행한다.
7-1) sum
	1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	2) 현재 노드 번호가 위치한 곳부터 1이 될 때까지 fenwick_tree에서 값을 접근하면 해당 노드까지의 거리가 되므로 node_loc이 1이 될 때까지 LSB를 빼주며 쿼리를 진행한다.
7-2) query
	1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	2) 해당 노드가 fenwick_tree에서 위치한 곳부터 최대 길이 n까지 LSB를 더해가며 fenwick_tree를 업데이트 한다. 
	3) 위의 과정을 거치면 업데이트하려는 특정 노드가 아닌 다른 특정 노드까지 가는 비용 또한 업데이트가 되므로 현재 노드와 해당 노드의 자식 수(child_node_count[node_number]) + 1부터 즉, 특정 노드의 subtree를 제외한 부분은 다시 update했던 값을 빼주며 fenwick_tree를 유지시킨다.
"""

"""
수행시간 분석
1. 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 각종 리스트를 만드는 데에 걸리는 시간은 O(n) + O(q) 
2. dfs로 전위순회를 하며 nodes_location, preorder_cost,child_node_count, path_sum 리스트들을 구하는 시간은 모든 노드만을 탐색하면 되기 떄문에 O(n) 시간이 걸린다.
3. dfs로 구한 path_sum 리스트를 사용해 dif 리스트를 만드는 데에 걸리는 시간은 O(n) 시간이 걸린다.
4. n개의 값이 저장된 dif 리스트를 이용해 fenwick_tree를 구성하는 데에 걸리는 시간은 O(nlogn) 시간이 걸린다.
5. sum 쿼리는 현재 노드부터 fenwick_tree에서의 1번 인덱스까지 접근하는데, 최대 logn번의 과정을 반복할 수 있기 때문에 O(logn) 시간이 걸린다.
6. update 쿼리는 값을 업데이트 하려는 노드부터 fenwick_tree의 끝까지 업데이트 하는 시간 O(logn)이 걸리고 값을 업데이트 하려고 하는 노드의 subtree가 아닌 노드들의 값을 다시 조정해주는 데에 O(logn) 시간이 걸려 2O(logn) 시간이 걸린다. 
7. sum 쿼리와 update 쿼리는 q만큼 실행하므로 O(qlogn) 시간이 걸린다. 
8. 위의 수행시간을 모두 더하고 간편화 하면 O(nlogn + qlogn)이 나오므로 수행시간은 O((n+q)logn)이다.
"""



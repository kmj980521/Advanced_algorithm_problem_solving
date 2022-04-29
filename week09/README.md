
# week7~9
## Prob1
- 조상 확인하기 
- 특정 노드 2개의 번호(u, v)를 query로 확인해 u노드가 v노드의 조상노드인지 찾는다.
- 자기는 자신의 조상노드이기도 하다.


### 해결 방법
- 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트를 선언한다. 
- n-1만큼의 입력을 받아 간선의 정보를 저장한다.
- q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
- 전위순회를 할 때 몇 번째로 방문했는지 저장할 변수인 pre_count와 특정 노드가 몇 번째로 방문을 했는지 값을 저장할 리스트 preorderList를 선언하고, 후위순회도 마찬가지로 post_count와 postorderList를 선언한다. 
- dfs_preorder를 거치며 전위순회를 하고 dfs_postorder를 거치며 후위순회를 해 preorderList와 postorderList를 완성시킨다.
- 그 후 쿼리에 대해서 각각의 리스트에 특정 노드의 번호(preorderList와 postorderList 인덱스 그대로 접근)에 대한 쿼리를 진행해 결과를 얻는다.
- confirm_ancestor.py


### 수행시간
- O(n) + O(q)


---

## Prob2
- 비용 합 질의
- n개의 노드와 m개의 에지로 구성된 트리 T가 입력으로 주어지면 T의 노드 v가 주어질 때, query_subtree(v)함수는 v의 부트리(subtree)에 포함된 노드의 비용을 모두 더한 값을 리턴한다.(단, v의 부트리에는 v도 포함된다)
- T의 노드 v가 주어질 때, query_update(v, d) 함수는 v의 비용을 d만큼 더한다.



### 해결 방법
- 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, 각 노드에 대해 자식수를 구할 child_node_count 리스트, 각 노드가 preorderList에 몇 번째에 위치하는지 값을 구할 수 있는 nodes_location 리스트, 방문 순서대로 cost를 저장할 preorder cost 리스트, preorder cost로 만들 fenwick 트리인 fenwick_tree_by_preorder_cost 리스트를 선언한다. 
- n-1만큼의 입력을 받아 간선의 정보를 저장한다.
- q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
- dfs를 전위순회를 하며 특정 노드의 방문 시간(nodes_location)과 언제 방문을 했는지(preorder_cost) 자기 cost를 append 하고 dfs를 수행할 때 마다 자식 수(child_node_count)를 구한다.
- dfs를 거치며 만들어지는 preorder_cost를 이용해 fenwick_tree(각각의 인덱스는 특정 노드 번호까지의 cost의 합을 fenwick_tree를 구현한 것)를 구현한다. 
- 그 후 각각의 쿼리에 대해 진행한다.
  1) update
		  	1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.
		  	2) 그 노드의 번호부터 fenwick_tree를 거치며 각각의 tree에 위치한 값에 update_cost를 더해주며 값을 업데이트 한다. 
  2) subtree
		  	1) preorder를 순회하고, cost를 기준으로 만든 fenwick_tree에서 (특정 노드의 위치 + 자식 수) - (특정 노드의 위치 - 1)이 자신의 subtree이므로, 현재 노드 번호가 preorderList에서 존재하는 위치(nodes_location)와 특정 노드의 자식 수(node_number)를 구한 all_of_subtree(특정 노드까지의 subtree)를 구한다.
		  	2) 현재 노드 번호가 preorderList에서 존재하는 위치(nodes_location) - 1 번째 위치는 특정 노드의 상위에 있는 node들을 제거한 값인 not_subtree(특정 노드의 상위 subtree들)를 구한다.
		  	3) all_of_subtree에 대해 fenwick_tree에 쿼리를 날려 각각의 값을 더해주며 sum 변수를 구해준다.
		  	4) not_subtree에 대해 fenwick_tree에 쿼리를 날려 위에서 구한 sum 변수에서 각각의 값을 빼주고 결과를 출력한다.
- query_sum_of_cost_with_fenwickTree.py

### 수행시간
- O((n+q)logn)


---

## Prob3
- 경로 합 질의
- n개의 노드와 m개의 에지로 구성된 트리 T가 입력으로 주어지면 T의 노드 v가 주어질 때, query_path(v)함수는 T의 루트 노드에서 노드 v까지의 경로에 있는 노드의 비용을 모두 더한 값을 리턴한다. 
- T의 노드 v가 주어질 때, query_update(v, d) 함수는 v의 비용을 d만큼 더한다.


### 해결 방법
- 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, 각 노드에 대해 자식수를 구할 child_node_count 리스트, 각 노드가 preorderList에 몇 번째에 위치하는지 값을 구할 수 있는 nodes_location 리스트, preorder dfs를 하며 방문하는 순서대로 노드의 cost를 저장할 path_sum 리스트, path_sum 리스트를 이용해 인접한 값의 차이를 저장할 dif 리스트, preorder cost로 만들 fenwick 트리인 fenwick_tree_by_dif 리스트를 선언한다. 
- n-1만큼의 입력을 받아 간선의 정보를 저장한다.
- q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
- dfs를 전위순회를 하며 특정 노드의 방문 시간(nodes_location)과 언제 방문을 했는지 preorderList에 append를 해주고 해당 노드의 cost를 path_sum리스트에 append하고, dfs를 수행할 때 마다 자식 수(child_node_count)를 구한다.
- 그 후 구한 path_sum 리스트를 이용해 인접한 값의 차이를 저장하는 dif 리스트를 만든다.
- dif 리스트를 이용해 fenwick_tree_by_dif라는 fenwick_tree를 만든다.
- 그 후 각각의 쿼리에 대해 진행한다.
  1) sum
  
	  1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	  2) 현재 노드 번호가 위치한 곳부터 1이 될 때까지 fenwick_tree에서 값을 접근하면 해당 노드까지의 거리가 되므로 node_loc이 1이 될 때까지 LSB를 빼주며 쿼리를 진행한다.
	  
  2) query
  
	  1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	  2) 해당 노드가 fenwick_tree에서 위치한 곳부터 최대 길이 n까지 LSB를 더해가며 fenwick_tree를 업데이트 한다. 
	  3) 위의 과정을 거치면 업데이트하려는 특정 노드가 아닌 다른 특정 노드까지 가는 비용 또한 업데이트가 되므로 현재 노드와 해당 노드의 자식 수(child_node_count[node_number]) + 1부터 즉, 특정 노드의 subtree를 제외한 부분은 다시 update했던 값을 빼주며 fenwick_tree를 유지시킨다.
- query_sum_of_path_with_fenwickTree.py


### 수행시간
- O((n+q)logn)

---

## Prob4
- 경로 합 질의
- n개의 노드와 m개의 에지로 구성된 트리 T가 입력으로 주어지면 T의 노드 v가 주어질 때, query_path(v)함수는 T의 루트 노드에서 노드 v까지의 경로에 있는 노드의 비용을 모두 더한 값을 리턴한다. 
- T의 노드 v가 주어질 때, query_update(v, d) 함수는 v의 비용을 d만큼 더한다.


### 해결 방법
- 최대 노드 수 n, 쿼리의 갯수 q를 입력받고, 노드 수 n에 따라 방문처리를 할 visited 리스트, graph, queries 리스트, 각 노드에 대해 자식수를 구할 child_node_count 리스트, 각 노드가 preorderList에 몇 번째에 위치하는지 값을 구할 수 있는 nodes_location 리스트, preorder dfs를 하며 방문하는 순서대로 노드의 cost를 저장할 path_sum 리스트, path_sum 리스트를 이용해 인접한 값의 차이를 저장할 dif 리스트, preorder cost로 만들 fenwick 트리인 fenwick_tree_by_dif 리스트를 선언한다. 
- n-1만큼의 입력을 받아 간선의 정보를 저장한다.
- q만큼의 입력을 받아 쿼리의 갯수를 저장한다. 
- dfs를 전위순회를 하며 특정 노드의 방문 시간(nodes_location)과 언제 방문을 했는지 preorderList에 append를 해주고 해당 노드의 cost를 path_sum리스트에 append하고, dfs를 수행할 때 마다 자식 수(child_node_count)를 구한다.
- 그 후 구한 path_sum 리스트를 이용해 인접한 값의 차이를 저장하는 dif 리스트를 만든다.
- dif 리스트를 이용해 fenwick_tree_by_dif라는 fenwick_tree를 만든다.
- 그 후 각각의 쿼리에 대해 진행한다.
  1) sum
	  1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	  2) 현재 노드 번호가 위치한 곳부터 1이 될 때까지 fenwick_tree에서 값을 접근하면 해당 노드까지의 거리가 되므로 node_loc이 1이 될 때까지 LSB를 빼주며 쿼리를 진행한다.
  2) query
	  1) 현재 노드 번호(node_number)가 preorderList에서 존재하는 위치(nodes_location)를 구한다.(node_loc)
	  2) 해당 노드가 fenwick_tree에서 위치한 곳부터 최대 길이 n까지 LSB를 더해가며 fenwick_tree를 업데이트 한다. 
	  3) 위의 과정을 거치면 업데이트하려는 특정 노드가 아닌 다른 특정 노드까지 가는 비용 또한 업데이트가 되므로 현재 노드와 해당 노드의 자식 수(child_node_count[node_number]) + 1부터 즉, 특정 노드의 subtree를 제외한 부분은 다시 update했던 값을 빼주며 fenwick_tree를 유지시킨다.
- query_sum_of_path_with_fenwickTree.py


### 수행시간
- O((n+q)logn)


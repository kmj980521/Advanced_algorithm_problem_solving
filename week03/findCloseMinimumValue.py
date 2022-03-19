n = int(input())
A = [int(x) for x in input().split()]


min_idx = -1
min_num = 99999999
B= []

for start in range(n):
    if A[start]<=min_num:
        min_num = A[start]
        min_idx = start
        B.append(0)
        continue
    else:
        for j in range(start, min_idx - 1, -1):
            if A[j] < A[start]:
                B.append(A[j])
                break

for element in B:
    print(element,end=" ")
		
"""
해결 과정
0. 리스트 자료구조를 이용했고 투포인터 기법을 사용했다  
1. start는 시작점, min_idx는 일종의 pointer이며 값들 중에 가장 작은 값을 저장하기 위해 사용한다
2. start 기준점부터 오른쪽으로 진행을 하는데 첫 if문에서 기존의 가장 작은 값인 min_num보다 더 작은 값이 온다면 min 값을 업데이트함과 동시에 start 기준 왼쪽 값들은 자기 자신보다는 반드시 크거나 같은 값이기 때문에 다른 연산 없이 0을 append 해준다
3. 그것이 아니라면 자기 위치(start)부터 거꾸로 min_idx까지(위의 if문을 거치지 않았다면 min_num은 반드시 자기 자신보다 더 작은 값이므로)탐색하며 자기 자신보다 작은 값을 찾아나간다 
"""
"""
수행시간 분석
0. 입력 및 변수 선언 O(1)
1. 최선의 경우)  min_num이 업데이트 되며 선형 시간 O(1)만큼 수행되며 n개의 원소가 실행되므로 O(n)
2. 최악의 경우) A= [3, 10, 9, 8, 7, 6, 5, 4]인 경우 처음 3만 선형 시간에 수행되지만 뒤에서 부터는 1 + 2 + 3 + 4 + ... + n-1번만큼 for문으로 이동하며 비교를 하기 때문에 O(n^2)이 될 수도 있다. 그러나 이 경우는 극히 드문 경우이다.
3. 마지막에 B리스트를 출력하는 시간 O(n)
"""
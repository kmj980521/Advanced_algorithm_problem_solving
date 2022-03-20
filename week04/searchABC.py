# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from bisect import bisect_left, bisect_right 
	
	
n = int(input())
A = []
for i in range(n):
	A.append(int(input()))

	
A.sort() # 1번 조건을 위해 오름차순으로 정렬한다 

count = 0

for i in range(n):
    for j in range(i+1,n):
        if A[i] == A[j]: break
        k = j+1 # a(A[i]), b(A[j]) 순서쌍에서 j값 다음에 오는 값을 판별하며 a,b,c를 찾는다 
        left_target = 2*A[j]-A[i] # 2번 수식을 전개 했을 때 2b -a <= c 이기 때문
        right_target = 3 * A[j] - 2 * A[i] # 2번 수식을 전개 했을 때 c <= 3b-2a 이기 때문에 
        left_idx = bisect_left(A,left_target,lo=k,hi=len(A)) # 2b-a 값이 리스트에 정렬 된 상태를 유지한채 들어간다고 가정했을 때 가능한 위치. 즉 left_target보다 크거나 같은 값의 위치를 찾기 위해 bisect_left를 사용
        right_idx = bisect_right(A,right_target,lo=k,hi= len(A)) # 3b-2a 값의 리스트에 정렬 된 상태를 유지한채 들어간다고 가정했을 때 가능한 위치. 즉 right_target보다 작거나 같은 값의 위치를 찾기 위해 bisect_right를 사용 
        count += (right_idx - left_idx)

print(count)

"""
해결 과정 
0. 리스트를 사용했고, 이를 오름차순으로 정렬한 후(1번 조건 만족을 위해) a,b 순서쌍을 먼저 선택한 후 c 값의 범위를(2번 조건을 전개해서) c보다 작거나 같은 값이 가능한 인덱스는 upper bound, c보다 크거나 같은 값이 가능한 인덱스는 lower bound로 찾아내 사이에 몇 개의 수가 가능한지 구해 O(n^2logn)에 구현했다.
1. n개의 숫자를 입력받아 A 리스트를 선언하고, 1번 조건인 a < b < c를 만족하기 위해 A를 오름차순으로 sorting 해주었다.
2. 2번 조건을 전개 하면 모든 항에 b를 더했을 때 '2b-a <= c <= 3b-2a' 라는 수식이 나온다. 이를 이용해 a는 A리스트의 0번째부터, b는 a위치 +1번째로 시작하며 순서쌍을 구해주고 a와 b가 결정이 됐다면 2b-a 값은 left_target, 3b-2a 값은 right_target으로 둔다.
3. j번째 숫자 다음부터 c값을 결정하기 때문에 k라는 변수에 j+1을 삽입한다.
4. 정렬 된 배열에서 정렬 된 순서를 유지하며 left_target을 삽입한다고 가정했을 때 가능한 위치 즉, left_target의 값보다 크거나 같은 값이 처음으로 나오는 위치를 이진 탐색으로 찾기 위해 bisect_left를 사용했고 반환값을 left_idx에 저장한다. -> (A 리스트에 대해, left_target을 삽입한다고 가정했을 때, low는 k 값 인덱스부터, high는 A의 리스트 길이 인덱스까지 가능한 값을 구한다)
5. 마찬가지로 right_target을 삽입한다고 가정했을 때 가능한 위치 즉, 이번에는 right_target의 값보다 작거나 같은 값이 처음으로 나오는 위치를 이진 탐색으로 찾기 위해 bisect_right를 사용했고 반환값을 right_idx에 저장한다.
6. 두 과정을 거치면 left_idx부터 right_idx 사이에는 2번 조건을 만족하는 c값들이 존재할 것이고, right_idx 값에서 left_idx를 빼주면 해당 인덱스값들 사이에 A 리스트에서 2번 조건에 부합되는 c 값이 되는 원소의 숫자들이 나오기 때문에 이 값을 count에 저장한다. 
"""

"""
수행시간 분석
1. 각종 변수를 선언하는 시간은 상수시간 O(1)
1. n개의 값을 입력받는 시간) 1개를 입력받는 데에 걸리는 시간은 O(!)이나 n개에 대해 실행하기 때문에 O(n) 수행시간이 걸린다
2. A에 대해 오름차순으로 정렬을 해주는데, python의 sort()는 O(nlogn) 수행시간을 갖는다.
3. k 값, left_target, right_target, count를 구하는 과정은 상수 시간인 O(1)에 가능하나, 이진 탐색으로 특정한 값을 찾는 것은 O(logn)의 수행시간을 갖는다. 이때, left와 right에 대해서 구해주기 때문에 O(2logn)이 걸릴 것이며 i는 n까지, j도 n-1 까지 돌기 때문에 2logn이 n(n-1)번 반복될 것이다. 즉 반복문은 O(n^2 * 2logn)의 수행시간을 갖는다. 
4. 위의 모든 경우를 더했을 때 nlogn + (n^2*2logn) + n + 1이 나온다.
5. 위의 값을 빅오로 표현하면 시간 복잡도에 더 영향을 주는 것은 n^2logn이기 때문에 전체적인 수행시간은 O(n^2logn)이다.
"""
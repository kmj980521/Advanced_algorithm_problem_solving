n,k = map(int,input().split())
A = [int(x) for x in input().split()]


B = []

min_num =99999999
min_num = min(A[0:k])
B.append(min_num)


for i in range(k,n):
    if A[i-k] == min_num: ## A[pointer-k] -> 빠져나가려는 기존 구간의 값이 min값이었다
        min_num = min(A[i+1-k:i+1]) # 거기서 min을 구한다
        B.append(min_num)
       # print("1번 조건 ")
    else:
       # print("2번 조건")
        if min_num > A[i]:
            min_num = A[i]
            B.append(min_num)
        else:
            B.append(min_num)

for element in B:
	print(element,end=" ")

"""
해결 과정
0. 리스트 자료구조를 이용했고 투포인터 기법을 사용했다.
1. k는 interval로 처음 범위에 대해서 min 값을 구한다(일종의 바닥조건) 
2. k번째부터 (k=4면 0~3번째 인덱스에서 min 값을 구하고 다음 인덱스인 4부터 시작) n까지 반복문을 돈다.
3. 첫 if문은 i-k는 이제 interval을 옮겨가는데 왼쪽에서 제외되려는 값이 min_num이면 새로운 범위에 대해서 min 값을 구하고 B에 append를 한다.
4. else 문에서 즉 min값이 interval 밖으로 나가지 않는다면 새로 들어오는 값 A[i]가 min값 보다 작은지 비교해 작다면 min값을 업데이트 시키고 그 값을 B에 append 시킨다.
5. 만약 새로 들어오는 값이 min값 보다 크다면 기존의 min 값을append 해준다.
"""
"""
수행시간 분석
0. 입력 및 변수 선언 O(1)
1. 처음 min_num을 구하는 수행시간 O(k)
2. 최선의 경우) n-k번의 루프를 돌며 모든 경우 min_num이 오며 상수시간만 걸리는 경우가 존재한다. min_num을 업데이트하고 B 리스트에 append하는 경우는 상수시간O(1)이기 때문에 수행시간은 O(n-k) = O(n)이다.
3. 최악의 경우) n-k번의 루프를 돌며 모든 경우에서 min_num 값을 새로 구해줘야 하는 경우가 존재한다. 이 경우에는 k 값만큼의 범위에서 min값을 구하기 때문에 min값을 구하는 수행시간은 k가 나올 것이고 k(n-k) = nk-k^2 수행시간이 걸릴 것이다. 그 후 k = 1일 때는, O(n)의 수행시간이 걸릴 것이고 k = n일 때는 n*n - n^2이기 때문에 0번의 loop가 반복될 것이고 처음 for loop 밖에서 min_num을 구하는 시간인 O(n)이 걸릴 것이다. 
4. 즉 O(n) 수행시간이 걸릴 것이다.
"""

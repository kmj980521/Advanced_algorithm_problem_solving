def solve(A):
    if len(A) <= 2:
        return A
    if A[1] < A[0]:
        A[0],A[1] = A[1], A[0]
    for i in range(1,len(A),2):
        if i == len(A)-1 :  #마지막
            if A[i-1] > A[i]:
                A[i-1],A[i] = A[i],A[i-1]
        else:
            if not (A[i-1]<=A[i] and A[i] >=A[i+1]):
                if A[i-1]<A[i+1]:
                    A[i],A[i+1] = A[i+1],A[i]
                else:
                    A[i],A[i-1] = A[i-1],A[i]
    return A
"""
동작 방식
0. 리스트의 길이가 2 이하라면 바로 return을, 그렇지 않으면 규칙을 맞춰주기 위해 [0]과 [1]을 비교해 [1]이 더 크다면 값을 교환한다. (일종의 바닥조건)
1. 조건상 [1], [3], [5] ... 즉 짝수번째 값들은 양 옆의 원소와 비교해 그 값보다 크거나 같은 값을 가지고 있으니 우선 for문에서 초기 시작을 1,  step을 2로 설정해 짝수번째 값들에 대해서 if를 실행한다
2. 만약 인덱스 i가 마지막 원소라면 그 직전의 값과 비교하여 만약 마지막 값이 더 작다면 값을 바꿔준다. 
3. step을 2씩 진행하며 각각 짝수번째 숫자와 양 옆의 숫자를 비교하여 양 옆보다 크다면 그대로, 그것이 아니라면 양 옆 중 더 큰 값으로 교환한다. 즉, 봉우리를 만들듯이 계속 값을 업데이트 해나가는 방식이다.
"""
"""
수행시간 분석
1. 처음 if에서 값을 바꾸는 시간 O(1)
2. n/2개의 원소에 대해서 각각 비교하교 교체하는 시간 O(1) 이지만 n/2 즉 O(n/2) = O(n)
3. 최종적으로 O(n) 시간이 걸린다. 
"""

def check(B):
    if not (B[0] <= B[1]): return False
    for i in range(1, len(B)-1):
        if i % 2 == 1 and not (B[i] >= B[i+1]):
            return False
        if i % 2 == 0 and not (B[i] <= B[i + 1]):
            return False
    return True

A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))
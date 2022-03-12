n, k = map(int, input().split())

A = [int(x) for x in input().split()]

find = False
pointer = 0
sum = 0

for start in range(n):
    while sum < k and pointer < n:
        sum += A[pointer]
        pointer += 1
    if sum == k:
        find = True
        break
    sum -= A[start]

if find:
    print(True)
else:
    print(False)

"""
해결 과정
0. 리스트 자료구조를 이용했고 일종의 투포인터 기법을 사용했다
1. start는 시작점, pointer는 끝점이다 
2. start 기준점을 잡고 pointer는 n보다 작을 때까지(끝까지) sum이 원하는 k보다 작을 때까지는 pointer를 증가시켜 값을 구하는 범위를 늘리게끔 한다. 
3. 만약 pointer가 끝까지 가거나, sum이 k값보다 크거나 같을 때 if문이 실행되며 만약 sum이 k와 같다면 찾았다는 의미로 find 변수를 True로 해준다.
4. 만약 sum이 k값이 아니라면 다음 시작점부터 이와 같은 과정을 반복해야 하는데 기존 시작점인 start 인덱스에 해당하는 값은 빼준다
"""
"""
수행시간 분석
0. 매 루프마다 항상 두 포인터 중 하나는 1씩 증가하고 있고, 각 포인터가 N번 누적 증가해야 알고리즘이 끝이난다
1. 즉 각각의 배열 끝에 다다르는 데에 O(n)이라 합쳐져도 O(n)이다.
"""
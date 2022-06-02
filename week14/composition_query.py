import sys
input = sys.stdin.readline

n = int(input()) # n 입력
fn = [0] + list(map(int, input().split())) # n개의 f(x)
num_of_query = int(input()) # 쿼리 수

sparse_table = [[fn[i]] for i in range(n + 1)]
#print(sparse_table)
for j in range(1, n + 1):
    for i in range(1, n + 1):
        sparse_table[i].append(sparse_table[sparse_table[i][j - 1]][j - 1])
# f(a, b, c) = f(a, (b, c)) = f(f(a, b),c)로 결합 법칙이 성립함을 이용 

for _ in range(num_of_query): # q의 반복
    x,pow_count = map(int, input().split())
    for a in range(pow_count, -1, -1): #log pow_count만큼의 반복 
        if pow_count >= 1 << a:
            pow_count -= 1 << a
            x = sparse_table[x][a]
    print(x)
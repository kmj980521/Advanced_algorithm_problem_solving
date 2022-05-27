def solve(A,n,tiles):
    DP = [[[0 for _ in range(tiles+1)] for _ in range(n+1)] for _ in range(n+1)]

    if n < 3 or n*(n//3) < tiles:
        return -1
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,tiles+1):
                if j<=2:
                    DP[i][j][k] = DP[i][0][k] = DP[i-1][n][k]
                else:
                    DP[i][j][k] = max(DP[i][j-3][k-1] + A[i-1][j-3] + A[i-1][j-2] + A[i-1][j-1], DP[i][j-1][k])
    return DP[n][n][k]






n,k = (int(x) for x in input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]
ans = solve(A,n,k)
print(ans)

"""
해결 방법 
- i는 행에서의 특정 열의 위치, j는 열에서의 특정 행의 위치, k는 타일의 수 
- 각 행에 대해, 각 열에 대해,각 칸을 DP로 따진다. 
- j <= 2라는 것은 타일을 둘 수 없는 i번째 행에서의 특정 열 위치이며 값을 업데이트 해준다.
- else : 해당 i,j,k는  타일을 두고 k-1개의 타일을 두었을 때의 값과 해당 위치 DP[i][j-3][k-1]과 타일을 두는 위치의 합과, 
j-1번째 열까지 진행을 하고 k개의 타일을 두었을 때의 max로 업데이트 
"""

"""
수행 시간

O(n^2 * k )
"""


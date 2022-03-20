def get_left_diagonal(row,col):
    possible_left = col
    possible_down = n-1-row
    returnValue = possible_down if possible_left>possible_down else  possible_left
    return returnValue

def get_right_diagonal(row,col):
    possible_right = n-1-col
    possible_down = n-1-row
    returnValue = possible_down  if possible_right > possible_down else possible_right
    return returnValue

def twoQueens():
    global count
    for row in range(n):
        for col in range(n):
            possible_case = (n**2 - 1) - (row*n) - col # 가능한 경우
            possible_case -= (n-1-col) # 같은 row에 존재하면 안 된다 
            possible_case -= (n-1-row) # 같은 column에 존재하면 안 된다
            possible_case -= get_left_diagonal(row,col) # 왼쪽 대각선에 위치하면 안 된다 
            possible_case -= get_right_diagonal(row, col) # 오른쪽 대각선에 위치하면 안 된다
            count += possible_case

n = int(input())

count = 0
A = [[0 for x in range(n)] for _ in range(n)]

twoQueens()

print(count)

"""
해결 과정 
0. 2차원 리스트를 사용했고, 첫 번째 Queen([row][col]위치)를 특정 위치에 두고 다른 Queen이 위치할 수 있는 경우의 수가 얼마나 되는지 판별한다. 
1. 이때 첫 번째 Queen은 0,0부터 시작하고 (0,1) (0,2) ... (0,n-1) 이렇게 column을 탐색하고 다음 row로 내려가는 방식이다. 또한, 첫 번째 Queen을 위치한다면 두 번째 Queen은 반드시 첫 번째 Queen이 거쳐온 자리는 체크하지 않는다. (왜냐하면 가능한 위치에서 Queen 서로 바꿔서 해도 같은 경우이기 때문. 불필요하게 2번 연산하는 것을 막는다.)

2. 입력받은 n을 이용해 n x n 2차원 리스트를 선언한다.
3. twoQueens() 메서드에서는 모든 row에 대해, 모든 column에 대해 가능한 경우를 모두 구해줄 것이다.
4. 첫 번째 Queen이 특정 위치에 있을 때 다른 Queen을 둘 수 있는 경우(possible_case)는 n*n의 공간에서 -1(첫 번째 Queen이 위치한 곳) 에서 길이가 n인 몇 개의 row를 거쳐왔는지 (row*n)를 빼주고 마지막으로 특정 row에 대해 column을 순차적으로 판별하기 때문에 지금까지 이동해 온 column의 값을 빼주면 첫 번째 Queen이 특정 [row][col]일 때 다른 Queen이 가능한 경우를 체크할 수 있다. 

5. 이 possible_case에서 4가지 경우를 생각해볼 수 있다. 1)첫 Queen과 같은 row에 존재하는 경우를 제외한다. 2)첫 Queen과 같은 column에 존재하는 경우를 제외한다. 3)첫 Queen과 같은 left_diagonal(왼쪽 대각선)에 존재하는 경우를 제외한다. 4)첫 Queen과 같은 right_diagonal(오른쪽 대각선)에 존재하는 경우를 제외한다.
5-1) 첫 Queen과 같은 row에 존재하는 경우) row는 그대로고 오른쪽으로 가며 남은 column의 수를 센다. 최종 길이는 n-1인데 여기서 현재 첫 번째 Queen의 column 위치인 col을 빼준다.
5-2) 첫 Queen과 같은 column에 존재하는 경우) column은 그대로고 밑으로 가며 남은 row의 수를 센다. 최종 길이는 n-1인데 여기서 현재 첫 번째 Queen의 row 위치인 row 값을 빼준다.
5-3) 첫 Queen과 같은 왼쪽대각선에 존재하는 경우) 왼쪽 대각선은 column 값은 감소하지만 row 값은 증가한다. 또한 첫 번째 Queen을 기준으로 (왼쪽으로 이동 가능한 거리 x 밑으로 이동 가능한 거리)를 계산했을 때 새로운 사각형이 만들어지는 것을 알 수 있다. 첫 번째 Queen의 col의 위치에서 봤을 때 Queen이 이동한만큼이 왼쪽으로 갈 수 있는 경우이다.(왜냐하면 col은 0부터 시작을 했고, 첫 번째 Queen이 2로 이동했다면 0,1해서 2이기 때문) 또한, 첫 번째 Queen의 row의 위치에서 봤을 때 Queen이 아래로 이동할 수 있는 경우는 n-1(최종 길이)에서 현재 row 위치 값인 row를 빼준다. 
이때 첫 번째 Queen의 왼쪽으로 이동 가능한 경우를 possible_left, 아래로 이동 가능한 경우를 possible_down 변수에 값을 저장하고, 대각선은 더 작은 값을 가진만큼만 이동이 가능하기 때문에 둘 중 더 작은 값을 반환해 가능한 경우에서 빼준다.
5-4) 첫 Queen과 같은 오른쪽대각선에 존재하는 경우) 오른쪽 대각선은 column 값도 증가하고 row 값도 증가한다. 4-3과 다른 점은 첫 번째 Queen을 기준으로 오른쪽으로 이동 가능한 거리를 구하는 것이기 때문에 전체 길이(n-1)에서 현재 첫 번째 Queen 위치한 column인 col을 빼준다. 첫 번째 Queen을 기준으로 밑으로 이동 가능한 거리는 5-3에서 구한 것과 마찬가지이며 이 또한 대각선을 구하는 것이기 때문에, 더 작은 값을 반환해 가능한 경우에서 빼준다.

6. 이와 같은 과정을 모든 row에 각각의 column에 대해 값을 구하고 첫 번째 Queen이 특정 [row][col]일 때를 기준으로 나머지 Queen이 올 수 있는 경우의 수를 count 변수에 더해간다.
"""

"""
수행시간 분석
1. 입력값 n에 대해 n x n 2차원 리스트를 만드는 수행시간은 O(n^2)이다. 
2. n을 입력받고, count를 선언하고, count를 print하는 과정은 상수시간 O(1)에 가능하다. 
2. 최종 possible_case를 구하는 과정은 전부 상수시간 O(1)에 가능하다. 
3. 이때, 모든 row, column에 대해 경우의 수를 구해줄 것이며, row와 column의 값은 n이고 n^2만큼의 반복문을 수행할 것이다.
4. 모든 경우를 합쳤을 때 2*n^2 + 1이 될 것이고, 이를 빅오로 표현하면 O(n^2)이 될 것이다.
5. 즉 O(n^2)의 수행시간을 가질 것이다. 
"""
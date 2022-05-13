import math

n, k = map(int, input().split())  # n -> 점의 수, k -> 색의 수

p_rainbow_count = [0] * (k + 1)  # 각 색의 수를 기록할 예정
outer_rainbow_count = [0] * (k + 1)  # p'

points = []

num_of_p_rainbow = 0  # 현재 p 무지개에는 몇 개의 색이 포함되어 있는지. 즉, 중복되지 않게 숫자가 들어가있는지 판별하고 그 색의 숫자를 기록
num_of_outer_rainbow = 0  # p' 무지개 기록

for i in range(n):
    point = int(input())
    if outer_rainbow_count[point] == 0:  # 즉, 현재 중복되지 않은 값일 때
        num_of_outer_rainbow += 1
    outer_rainbow_count[point] += 1
    points.append(point)
# print(points,outer_rainbow_count,num_of_outer_rainbow )

result = math.inf
start = 0
end = 0

while start <= end < n:
    # p rainbow가 k보다 작다면 뒤를 늘려 범위값을 늘려준다
    # p' outer rainbow가 k보다 크거나 같다면 끝을 늘려주기 때문에 범위가 줄어드는 것이다


    ### 여기 오른쪽에 =를 지우면 됨!

    if num_of_p_rainbow != k or num_of_outer_rainbow > k:
        # 현재 포인트 정보. 뒤를 늘려줄 것이기 때문에 end를 사용
        point_info = points[end]
        # 해당 점 카운트 1증가
        p_rainbow_count[point_info] += 1
        # 해당 점 카운트 1 감소
        outer_rainbow_count[point_info] -= 1

        # 만약 증가한 카운트가 1이라면, 즉 기존에 중복되지 않은 값과 다른 새로운 값이라면 num_of_p_rainbow에 존재하는 색의 수를 1증가
        if p_rainbow_count[point_info] == 1:
            num_of_p_rainbow += 1
        # 만약 감소한 카운트가 0이라면, 즉 기존에 중복되지 않은 값들에서 제외시켰을 때 0개가 된다는 것은 아예 빠져버리는 경우 -> num_of_outer_rainbow에 존재하는 색의 수 감소
        if outer_rainbow_count[point_info] == 0:
            num_of_outer_rainbow -= 1
        end += 1
    ## 반대의 경우에는 시작점을 움직여 줌.
    else:
        point_info = points[start]
        p_rainbow_count[point_info] -= 1
        outer_rainbow_count[point_info] += 1
        if p_rainbow_count[point_info] == 0:
            num_of_p_rainbow -= 1
        if outer_rainbow_count[point_info] == 1:
            num_of_outer_rainbow += 1
        start += 1

    if num_of_p_rainbow == num_of_outer_rainbow == k:
        result = min(result, end - start)

if result == math.inf:
    print(0)
else:
    print(result)

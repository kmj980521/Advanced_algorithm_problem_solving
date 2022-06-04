n, L, k = map(int, input().split())  # n = 좀비 수, L = 땅의 길이
zombie = []  # 좀비의 처음 위치를 기준으로 떨어질 때 까지의 시간을 계산하여 정렬할 list
before = []  # 좀비의 처음 위치를 일직선으로 정렬할 리스트
fall = []  # 떨어지는 좀비를 저장하는 list
i, j = 0, n - 1  # 절벽의 좌, 우를 나타내는 변수

for x in range(n):
    locate, id = map(int, input().split())
    zombie.append([id, locate])
    before.append([id, locate])

before.sort(key=lambda x: (x[1], x[0]))  # 현재 위치별로 정렬 O(nlogn)

for x in range(0, n):
    if zombie[x][0] > 0:
        zombie[x][1] = L - zombie[x][1]
zombie.sort(key=lambda x: (x[1], x[0]))  # 방향과 거리를 생각해서 저장한 리스트의 정렬 O(nlogn)

for x in range(0, n):  # O(n)
    if x <= n - 2 and zombie[x][1] == zombie[x + 1][1]:  # 동시에 떨어지는 좀비의 경우 아이디가 작은 순서로 두 좀비의 위치를 바꿔준다
        if zombie[x][0] > 0 and before[i][0] < before[j][0]:
            before[i], before[j] = before[j], before[i]
        elif zombie[x][0] < 0 and before[i] > before[j]:
            before[i], before[j] = before[j], before[i]
    if zombie[x][0] > 0:  # id가 양수인 경우
        fall.append(before[j][0])  # 오른쪽에 있는 좀비가 떨어진다
        j -= 1
    else:  # id가 음수인 경우
        fall.append(before[i][0])  # 왼쪽의 좀비가 떨어진다
        i += 1

print(fall[k - 1])  # k번째로 떨어진 좀비 출력
from collections import deque

n,L,k = map(int,input().split())
zombies = deque()

for i in range(n):
    location, id = map(int, input().split()) # 좀비 위치와 id를 입력 받음 
    if id < 0: # id가 음수면 왼쪽 -1, 양수면 오른쪽 1로 이동 
        direct = -1
    else:
        direct = 1
    zombies.append([location, id, direct])

outZombies = []

while len(outZombies)<k: # out된 좀비의 수가 k와 같아질 때 멈춘다 
    prev = ""
    min_time = L + 2 # 현재 좀비들의 위치에서 일어날 수 있는 이벤트를 처리하는 데에 걸리는 최소의 시간 
    for i in range(len(zombies)): # 모든 좀비들을 순회하며 
        if prev == "":  # 아무런 짝을 못찾았을 때 
            if zombies[i][2] == -1: # 좀비의 방향이 왼쪽이라면?
                if min_time > zombies[i][0] + 1: # 왼쪽 끝 + 1 만큼 걸리는 시간이 최소 시간일 때 업데이트를 해준다 
                    min_time = zombies[i][0] + 1
            else: # 좀비의 방향이 오른쪽이라면? 
                if min_time > L - zombies[i][0] + 1:  # 오른쪽 끝 + 1 만큼 걸리는 시간이 최소 시간일 때 업데이트를 해준다
                    min_time = L - zombies[i][0] + 1
                prev = '+'
        elif prev == '+' and zombies[i][2] < 0: # 만약 오른쪽으로 이동하는 좀비를 직전에 찾았고, 다음에 오는 좀비의 방향이 왼쪽일 때 즉, 서로 만날 가능성이 있다면 
            if min_time > (zombies[i][0] - zombies[i-1][0]) // 2: # 두 좀비의 거리의 차 // 2 를 한 값이 최소 시간일 때 업데이트를 해준다 
                min_time = (zombies[i][0] - zombies[i-1][0]) // 2
            if min_time == 0: # 만약 좀비가 충돌해서 방향을 바꾸려고 한다면? 마주치기 직전 or 이미 마주친 상태라면?
                if zombies[i][0] - zombies[i-1][0] == 1:  # ex) 12/13에 위치한 좀비가 이제 마주치려 한다면? 
                    zombies[i][0] += (zombies[i][2]) # 우선 서로 1칸씩 그대로 이동하고, 추후에 방향바꿔 1칸을 이동하면 같은 결과를 보인다! 
                    zombies[i-1][0] += (zombies[i-1][2])
                    zombies[i][2] = zombies[i][2] * -1
                    zombies[i-1][2] *= zombies[i-1][2] * -1
                if zombies[i][0] - zombies[i-1][0] == 0:  # ex) 13/13에 위치한 좀비가 존재한다면? 
                    zombies[i][2] = zombies[i][2] * -1 # 서로 방향만 바꿔준다 
                    zombies[i-1][2] = zombies[i-1][2] * -1
            prev = "" # 좀비 짝을 이루었으니 상태를 초기화 
        elif prev == '+' and zombies[i][2] > 0: # 만약 오른쪽으로 가는 좀비를 찾은 상태에서 또 오른쪽으로 가는 좀비를 찾았다면? 
            if min_time > L - zombies[i][0] + 1: # 해당 좀비가 오른쪽으로 가서 떨어지는 시간이 현재 최소 시간보다 작다면 업데이트 
                min_time = L - zombies[i][0] + 1
    this_time_out_zombies_count = 0
    i = 0
    while i < len(zombies):
        if min_time == 0:  # 좀비가 교차하는 경우에도 사실은 1 타임이 소요되어야 한다. 
            min_time = 1  
        zombies[i][0] += (zombies[i][2] * min_time)  # 소요 시간만큼 좀비들을 이동시킨다 
        if zombies[i][0] < 0 or zombies[i][0] > L:  # 좀비가 만약 out 되면?
            this_time_out_zombies_count += 1  # 동시에 떨어진 좀비수를 ++
            outZombies.append(zombies[i][1])  # 좀비 id를 append
            if zombies[i][0] < 0 : # 만약 왼쪽에서 떨어진 좀비라면? 
                zombies.popleft() # popleft 
                i -=1 # idx를 -1 해줘서 다음 좀비에 대한 판별을 이어간다 
            else:
                zombies.pop() # 오른쪽에서 떨어진 좀비라면 pop
        i +=1
    if this_time_out_zombies_count == 2:  # 만약 동시에 떨어진 좀비가 2마리라면?
        if outZombies[len(outZombies) - 1] < outZombies[len(outZombies) - 2]:  # 뒤늦게 들어온 좀비의 id 값이 더 작다면?
            outZombies[len(outZombies) - 2], outZombies[len(outZombies) - 1] = outZombies[len(outZombies) - 1], \
                                                                               outZombies[len(outZombies) - 2]  # 스왑
print(outZombies[k-1])
"""
해결 과정
1. 기본적인 알고리즘은 좀비에게 특정 이벤트(좀비가 왼쪽으로 떨어지거나, 오른쪽으로 떨어지거나, 또는 두 좀비가 만나 방향을 바꾸게 되는 이벤트가 일어난다거나)가 일어날 때까지의 최소 시간 min_time을 구해 1초마다 for를 돌리는 것이 아닌, 한 번에 좀비들을 이동시켜주는 방식이다. 또한, 좀비들이 짝을 이룰 때 (+ 방향으로 가는 좀비가 있다면 반드시 그 다음에 - 방향으로 가는 좀비가 있어야 충돌이 일어난다)를 이용할 것이다. 
2. 처음엔 좀비의 위치와 id를 입력 받고 그 id에 맞는 방향(direct) 값도 저장한다.
3. 큰 while 문에서는 outZombies(떨어져나간 좀비의 id를 저장하는 리스트)의 길이가 k와 같아질 때 종료를 하게 한다. 또한, 현재 판별 상태를 저장하기 위해 prev라는 변수를 선언했다. 
4. zombies Deque에 저장된 좀비들의 위치를 보며 min_time을 구해준다.
4-1. 짝을 이룬 상태인 prev에 값이 없는 상태 즉, 이전에 충돌 및 왼쪽으로 가는 좀비들을 봐온 상태에서 좀비의 방향이 -1 이라면? -> 왼쪽 끝으로 떨어진다고 생각하고 그 거리를 구해 현재 min_time보다 작다면 업데이트 한다.
4-2. 짝을 이룬 상태인 prev에 값이 없는 상태에서 좀비의 방향이 +1 이라면? -> 오른쪽 끝으로 떨어진다고 생각하고 그 거리를 구해 현재 min_time보다 작다면 업데이트를 하고 prev를 +로 바꿔준다.
4-3. prev의 값이 +인 상태 즉, 판별할 좀비의 이전 좀비가 오른쪽으로 이동하고 있는 좀비일 때, 현재 좀비의 방향이 -1 이라면? -> 서로 충돌할 가능성을 고려한다. 두 좀비 사이의 거리 //2의 값이 현재 min_time보다 작다면 업데이트 한다. 
4-3-1. 만약 min_time이 0이고, 두 좀비 사이의 거리가 1일 때 즉, 예를 들어 12 위치에 + 방향으로 이동하는 좀비가 있고, 13 위치에 - 방향으로 이동하는 좀비가 있다면 우선 서로 1칸씩 그대로 이동하고 추후에 방향을 바꿔 1칸씩 이동하면 자기 원래 위치에서 방향을 바꾼 것과 같게 되므로 우선 그대로 1칸 더 이동을 한 후에 방향을 바꿔준다. 
4-3-1. 만약 min_time이 0이고, 두 좀비 사이의 거리가 0일 때 즉, 예를 들어 13 위치에 + 방향으로 이동하는 좀비, 13 위치에 - 방향으로 이동하는 좀비가 겹쳐져 있다면, 서로 방향을 바꿔준다. 
4-5. prev 값이 +인 상태 즉, 판별할 좀비의 이전 좀비가 오른쪽으로 이동하고 있는 좀비일 때, 현재 좀비의 방향이 +1 이라면? -> 서로 같이 오른쪽으로 가서 떨어진다고 생각하고 현재 좀비가 떨어지는 시간을 구해 min_time보다 작다면 업데이트한다. 
5. 이후 this_time_out_zombies_count라는 변수를 두며 모든 좀비에 대해 판별이 끝난 후 좀비를 이동시킬 때 양 옆으로 떨어지는 좀비의 수를 count할 변수를 선언한다. 
6. 현재 남아있는 zombie의 수만큼 while을 돌 것이고, min_time이 0일 때, 즉 위에서 좀비의 방향이 교차할 때 사실은 1 타임이 소요되고 이동을 해야하기 때문에 min_time은 1로 설정한다.
7. 특정 이벤트가 일어나는 시간인 min_time과 각 좀비의 방향을 곱해 현재 좀비 위치에 더해준다면 소요시간만큼 좀비가 이동한 것이다. 
8. 좀비가 만약 0보다 작은 값 즉, 왼쪽으로 떨어지거나 L 보다 큰 값 즉, 오른쪽으로 떨어진다면 this_time_out_zombies_count 변수에 1을 더하고, 이 좀비의 id를 outZombies에 append 한다. 
9. 만약 좀비가 왼쪽으로 떨어졌다면 popleft()를 하고 popleft를 하면 자동으로 다음 좀비가 0번째 좀비가 되므로 이 좀비를 다음 loop에서 판별해주기 위해 i의 값을 1 감소시킨다.
10. 만약 좀비가 오른쪽으로 떨어졌다면 pop()을 해준다.
11. 만약 이번 loop 에 떨어진 좀비의 수가 2라면? -> 맨 뒤 좀비와 그 앞의 좀비의 id를 비교해 더 작은 좀비가 먼저 떨어진 것으로 하기 위해 swap을 해준다. 
"""
"""
수행시간 분석
1. n 마리의 좀비에 대한 정보를 입력받는 데에 O(n)의 수행시간이 필요하다.
2. 좀비가 1마리일 때 가능한 충돌 횟수는 0, 2마리일 때는 1, 3마리일 때는 2, 4마리일 때는 4, 5마리일 때는 6, 6마리일 때는 9, 7마리일 때는 12, 8마리일 때는 16 .... 이와 같이 있을 때 점화식을 구해준다면 n^2 // 4를 한 값에서 정수만 본다면 이 경우가 나오게 된다.  또한 각각의 경우에서 좀비가 떨어져 나가는 경우의 수는 n이므로 큰 while 문은 O(n^2//4) + O(n)이 될 것이며 더 큰 O(n^2//4)가 될 것이다. 
3. 모든 좀비들을 보며 특정 이벤트가 일어나는 최소 시간 min_time을 구하는 시간은 n마리의 좀비를 순회하기 때문에 O(n)이다.
4. 또한, min_time을 구한 후 좀비들을 이동 및 떨어져나가는 좀비를 판별할 때 최대 n마리의 좀비에 대해 판별하기 때문에 이 또한 O(n)이다.
5. 즉, while은 n^2//4 번 도는데 각 경우엔 최대 2O(n)이 걸리기 때문에 전체적인 수행시간은 n^3이 될 것이다.
6. 수행시간은 O(n^3)
"""
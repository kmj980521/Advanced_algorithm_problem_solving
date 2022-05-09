def solve(a, b, t):
    if a > b:
        long_time, short_time = a, b
    else:
        long_time, short_time = b, a
    max_number_of_eat_longtime_chicken = (t // long_time) + 1
    result_find_zero_time = 0 # 시간에 딱 맞춰 치킨을 먹을 때 가능한 경우의 수
    result_not_zero_time = 0 # 시간에 맞춰 치킨을 먹지 못할 때 가능한 경우의 수
    min_times = t+1 # 맥주를 마시는 데에 최소로 걸리는 시간
    flag = False
    for longtime_chicken_count in range(max_number_of_eat_longtime_chicken):
        remaining_time = (t - long_time * longtime_chicken_count) % short_time # 전부 다 먹고 남은 시간
        number_of_possible_case = longtime_chicken_count + (t - long_time * longtime_chicken_count) // short_time # 모든 치킨을 먹는 가능한 경우의 수

        if remaining_time == 0: # 치킨을 정확한 시간에 먹을 수 있을 때
            flag = True # 시간을 맞춰 먹을 수 있다는 Flag True
            min_times = 0 # 최소 시간은 0
            if result_find_zero_time < number_of_possible_case: # 기존에 치킨을 딱 맞춰 먹었을 때 가능한 경우의 수보다 더 많은 경우의 수를 찾는 다면 업데이트
                result_find_zero_time = number_of_possible_case
        elif remaining_time > 0 and not flag: # 치킨을 먹고 남는 시간이 존재할 때
            if min_times > remaining_time: # 남는 시간이 기존에 제일 최소로 맥주를 마시는 시간보다 더 작다면 즉, 치킨을 더 오래동안 먹는 경우라면 ?
                min_times = remaining_time # mintime을 업데이트
                result_not_zero_time = number_of_possible_case # 가능한 경우의 수 저장


    if flag:
        print(result_find_zero_time)
    else:
        print(result_not_zero_time, min_times)


# a는 후라이드
# b는 양념
# t는 시간
a, b, t = [int(x) for x in input().split()]
solve(a, b, t)
"""
해결 과정
1. 기본적인 알고리즘은 a와 b치킨 중 먹는 데에 시간이 더 오래걸리는 치킨을 선정해 그 치킨(long_time)을 t 시간내에 가장 많이 먹는 경우(t//long_time)의 수를 구해주고, 이 치킨을 0개부터 최대값까지 먹는 경우의 수를 for문으로 돌며 각각의 경우에 대해 시간이 적게 걸리는 치킨을 얼마나 먹을 수 있는지 구해(t - long_time * longtime_chicken_count) % short_time) 남은 시간(remaining_time)을 기준으로 t 시간에 맞춰 치킨을 먹을 수 있는지, 혹시나 시간이 남으면 최소로 맥주를 마시는 시간이 얼마나 되는지 구해준다.
2. 시간이 오래 걸리는 치킨의 수 + 시간이 적게 걸리는 치킨의 수인 number_of_possible 변수와 두 치킨을 먹고 남은 시간 remaining_time 변수를 이용한다.
3. remaining_time 즉, 치킨을 t 시간내에 정확하게 먹는 조합이 존재한다면 시간을 맞춰 먹을 수 있다는 bool 값 flag를 true로 정하고, 만약 현재까지 저장된 가능한 경우의 수보다 더 많은 수의 치킨을 먹는다면 값을 업데이트 한다. 
4. 만약 remaining_time이 0보다 크고 아직 정확한 t 시간에 치킨을 먹는 경우의 수가 존재하지 않았다면 현재까지 저장된 min_time 즉, 맥주 마시는 시간이 최소인 경우를 계속 업데이트 해나간다.
5. 그 후 flag bool 변수를 보고 true면(정확한 시간에 치킨을 먹는 경우) result_find_zero_time 값을, false면(정확한 시간에 치킨을 먹지 못하고 맥주를 마시는 시간이 최소인 경우) result_not_zero_time과 그때의 맥주를 마시는 최소 시간인 min_times를 출력한다.
"""
'----------------------------------------------'
"""
수행시간 분석
1. 각 변수를 선언하는 데에 걸리는 시간은 O(1)
2. 먹는 데에 시간이 오래 걸리는 치킨을 기준으로 t//long_time 만큼의 반복문을 돈다. 이때, long_time 변수의 값을 q라고 가정. 즉 t//q 만큼의 반복문을 수행한다. 
3. t//q 만큼의 반복문을 수행하며 모든 경우의 수를 구해주는 연산들은 상수시간에 가능하므로 반복문의 수행시간은 결국 O(t//q)가 될 것이다.
4. 즉 최종 수행시간은 먹는 데에 시간이 오래 걸리는 치킨의 시간을 q라고 보았을 때 O(t//q)가 될 것이다.
"""
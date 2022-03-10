inputStack = []
maxValStack = []
max_idx = 0
max_num = -999999
maxValStack.append(max_num)


while True:
    inputValue = input().split()
    command = inputValue[0]
    if command =="push":
        value = int(inputValue[1])
        inputStack.append(value)
        if value>max_num:
            max_num = value
            max_idx += 1
            maxValStack.append(value)

    elif command =="pop":
        if len(inputStack) == 0:
            print("EMPTY")
            continue
        else:
            outputValue = inputStack.pop()
            if outputValue == maxValStack[max_idx]:
                maxValStack.pop()
                max_idx-=1
                max_num = maxValStack[max_idx]
        print(outputValue)
    elif command =="max":
        if max_idx == 0:
            print("EMPTY")
        else:
            print(maxValStack[max_idx])
    elif command =="exit":
        break

"""
동작 방식
0. inputStack은 값들을 담을 스택, maxValStack은 최대값의 정보를 저장하기 위한 스택, max_idx는 maxValStack에서 현재 스택에서 최대값의 정보를 담고 있는 index, max_num은 최대값을 의미한다.
1. maxValStack [0]에 초기값 -999999를 대입하고 max_idx를 0으로 설정한다.
2. 명령어와 값을 입력 받는다.
2-1. push일 때) 값을 변환해서 push하며 기존의 최대값과 새로 삽입하려는 값을 비교해 새로 삽입하려는 값이 더 크다면 최선 정보로 업데이트 한다
2-2. pop일 때) inputStack 길이가 0이면 EMPTY를 출력하고, 스택에 값이 남아있다면 pop을 하고 이 값이 기존 스택에 최대값이라면 최신화하며 값을 갱신했던 maxValStack에서 pop을 하고 최신화 한다
2-3. max일 때) inputStack 길이가 0이면 EMPTY를 출력하고, 스택에 값이 남아있다면 최대값의 정보를 담고 있는 max_idx를 이용해 현재 스택의 최대값을 출력한다
2-4. exit일 때) 프로그램을 종료한다 
"""

"""
수행시간 분석
1. 각 원소에 대해 push 하는 경우 평균 시간은 O(1)이지만 n개의 원소에 대해서 실행하기 때문에 O(n)
2. 각 원소에 대해 pop 하는 경우 평균 시간은 O(1)이자만 n개의 원소에 대해서 실행하기 때문에 O(n)
3. 각 원소에 대해 max를 하는 경우 스택의 특정 위치 정보(max_dix)를 이용해 조회를 하기 때문에 평균 시간은 O(1) 만약 n개의 원소에 대해 실행하면 O(n)

4. 모든 경우를 모두 더해도 수행시간은 O(n)이다
"""
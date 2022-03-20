# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

A = [ int(x) for x in input().split()]

electedPersonIdx = -1 # 당선된 시장 후보 번호
mydict = {} # 시장 후보를 저장하기 위한 dict
find = False # 당선인 찾은 여부 

for i in A: # 모든 A의 element에 대해서 
    if i not in mydict: # dict에 없다면 i:1 , 즉 i번 후보가 1표를 받았다는 것을 표시한다 
        mydict[i] = 1
    else:
        mydict[i] = mydict[i] + 1 # 만약 기존 dict에 존재한다면? i번 후보 키 값에 대해 value를 얻어와 1을 더해 새로운 value를 지정한다 

dict_lis = mydict.items() # 번호 취합 후 (후보번호-value(득표수)) -> 인 튜플을 얻는다 


for person in dict_lis: 
    if person[1] > n/2: # 사람에 대해 [1] ->  득표수가 전체 인원수 / 2보다 크다면 즉, 과반수라면? 
       electedPersonIdx = person[0] # 그 사람의 번호 [0]는 당선된 시장의 후보 번호였다
       break

print(electedPersonIdx)

"""
해결 과정 
0. 딕셔너리를 사용해 메모리를 효율적으로 관리하고 특정 후보자가 몇 표를 받았는지 빠르게 정보를 알 수 있게 했다.
1. 시장 후보의 정보를 저장하기 위한 mydict 딕셔너리를 선언했고 (key-value) 쌍은 (후보 번호-득표수)로 관리할 것이다. 
2. A 리스트를 돌며 특정 후보자의 번호를 하나씩 받아오고 이 번호가 키 값으로 존재하지 않는다면 새로운 1표를 받았다는 의미로 mydict에 새로 삽입한다.
3. 만약 mydict에 존재한다면 value 값을 얻고, value 값에 +1을 해준다.
4. 그 후 mydict에서 (key-value) 쌍으로 이루어진 투플들이 담긴 리스트를 dict_lis에 반환받는다.
5. 리스트를 순환하며 person[1] (value=득표수)가 n/2 즉, 과반수 초과라면 해당 시장 후보의 번호(person[0])를 당선인 후보 번호(electedPersonIdx)에 저장하고 마지막에 출력한다.
"""
"""
수행시간 분석
1. 각종 변수를 선언하는 시간은 상수시간 O(1)
2. 입력받은 n에 대해 리스트를 선언하는 시간은 O(n)
3 A 리스트를 돌며 mydict에 값을 업데이트 해가는 경우) mydict에 접근 및 삽입은 O(1)은 가지는데 n개의 정보가 담긴 리스트 A만큼 실행되기 때문에 O(n) 수행시간을 갖는다.
4. mydict의 정보를 dict_lis로 변환하는 과정은 mydict의 key-value 쌍의 수인데, 최악의 경우 n개의 key-value 쌍이 저장될 수 있기 때문에 이 과정도 O(n) 수행시간을 갖는다.
5. dict_lis를 순회하며 당선인을 판별할 때 2)의 경우에서 n개의 key-value 쌍이 나올 수 있다고 했기 때문에 각종 비교 및 삽입은 O(1) 가지는데 이를 n번 실행하기 때문에 O(n) 수행시간을 갖는다.고
6. 종합적으로 4n+1이 나올 것이고, 이를 빅오로 표현하면 O(n) 수행시간을 갖게 될 것이다.
"""
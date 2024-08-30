import statistics
from collections import Counter
a = int(input()) #입력값 받기
arr1 = [] #배열 초기화
for i in range(a):  #A만큼 배열의 요소를 받고 배열에 추가
    ab = int(input())
    arr1.append(ab)

if a == 1:        #배열의 길이가 이면 그대로 출력
    print(ab)
    print(ab)
    print(ab)
    print(0)
else:
    sum = 0         #평균을 출력하기 위한 변수
    for i in arr1:   #배열에 있는 모든 수 합하기
        sum += i
    avg = sum / len(arr1)   #산술평균 구하기
    print(round(avg, 1))    #round로 반올림해서 출력
    arr1.sort()  #배열 정렬
    print(arr1[len(arr1) // 2])  #배열의 중간 위치값 구하기

    counter = Counter(arr1)    #배열의 요소들의 출현 빈도수를 알려준다.

    arr_mode = counter.most_common()[1] #제일 많은 배열의 2번째로 작은 수를 출력한다.
    print(arr_mode[0])  #두번쨰로 작은 수 출력




    print(arr1[len(arr1) -1] - arr1[0])
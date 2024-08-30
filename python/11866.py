import sys
n, k = map(int, sys.stdin.readline().split()) # n과 k를 입력받음
list1 = []     #1번부터 n번까지의 배열
result = []    #요세푸스 순열 배열
for i in range(n):    #list1배열 초기화
    list1.append(i+1)
index = 0      #번호 초기화
for i in range(n):
    index += k - 1   #k번쨰 사람
    if index >= len(list1):  #index가 list1의 크기를 벗어나면 나머지를 이용해 원형배열처럼 사용
        index %= len(list1)
    result.append(str(list1.pop(index)))  #list1배열에서 index순서의 요소 삭제후 삭제한 값을 result배열에 추가
    


print("<", ", ".join(result), ">", sep="") #,로 result배열을 입력해서 정답 출력

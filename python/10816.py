# n 숫자의 개수 입력
n = int(input())
# n개의 숫자 입력
n_list = list(map(int, input().split()))
# n_list 정렬
n_list.sort()
# m 숫자의 개수 입력
m = int(input())
# m개의 숫자 입력
m_list = list(map(int, input().split()))

# 같은 카드를 몇 개 가지고 있는지 딕셔너리로 정리
count = {}
for n_count in n_list:
    if n_count in count:
        count[n_count] += 1
    else:
        count[n_count] = 1

# 이분탐색
def counting(n_list, index_m, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    if n_list[mid] == index_m:
        return count.get(index_m)
    elif n_list[mid] < index_m:
        return counting(n_list, index_m, mid + 1, right)
    else:
        return counting(n_list, index_m, left, mid - 1)

for result in m_list:
    print(counting(n_list, result, 0, len(n_list)-1), end=" ")

arr = ['a', 'b', 'c', 'd', 'e', 
       'f', 'g', 'h', 'i', 'j', 
       'k', 'l', 'm', 'n', 'o', 
       'p', 'q', 'r', 's', 't', 
       'u', 'v', 'w', 's', 'y', 'z']

s, skip, index = map(str, input().split())
index = int(index)


def solution(s, skip, index):

    keep = []
    for j in range(len(skip)):
        for i in range(len(arr)):
            if skip[j] == arr[i]:
                keep.append(i)
                break

    keep.sort(reverse=True)
    for i in keep:
        del arr[i]

    keep1 = []
    for j in range(len(s)):
        for i in range(len(arr)):
            if s[j] == arr[i]:
                keep1.append(i)
                break

    result_arr = []
    for i in keep1:
        result_arr.append(arr[(i+5) % len(arr)])
        
    result_str = ''.join(result_arr)
    return result_str

result = solution(s, skip, index)
print(result)






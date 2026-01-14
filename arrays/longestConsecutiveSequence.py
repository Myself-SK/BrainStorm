# arr = [100,4,200,1,3,2]
# arr = [0,3,7,2,5,8,4,6,0,1]
# arr = [1,0,1,2]
# arr = [1, 2, 6, 7, 8]
arr = [1, 2, 3, 4, 100, 200]
def longest_consecutive_sequence(arr:list)->int:
    arr = list(set(arr))
    arr.sort()
    if len(arr)>=1:count=1
    else: count=0
    max_count = []
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i])==1:
            count+=1
        if (arr[i+1] - arr[i]) > 1:
            max_count.append(count)
            count=1
    max_count.append(count)
    return max(max_count)

print(longest_consecutive_sequence(arr))

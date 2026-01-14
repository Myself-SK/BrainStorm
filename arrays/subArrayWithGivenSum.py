# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# arr = [1, 10, 4, 0, 3, 5]
# arr = [12, 18, 5, 11, 30, 5]
arr = [19,23,15,6,6,2,28,2]

def sub_array_with_sum(arr:list,target:int)->list:
    res = []
    for i in range(len(arr)):
        if arr[i]<target:
            for j in range(i+1,len(arr)+1):
                print(sum(arr[i:j]))
                if(sum(arr[i:j]) == target):
                    res = [i+1,j]
                    return res
                if(sum(arr[i:j])> target):
                    break
        if arr[i]==target:
            return [i+1,i+1]
    return [-1]

# print(sub_array_with_sum(arr,23))
# print(sub_array_with_sum(arr,7))
# print(sub_array_with_sum(arr,69))
print(sub_array_with_sum(arr,2))
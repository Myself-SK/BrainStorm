# l = [1, 3, 3, 5, 4]
# l = [2, 2]
# l = [1, 3, 3] 
l = [4, 3, 6, 2, 1, 1]

def find_missing_and_repeating_number(arr:list)->int:
    max_value = max(arr)
    miss_value = 0
    repeating_value = arr[0]
    for i in range(1,max_value+1):
        if i not in arr:
            miss_value = i
        if arr.count(i)>1:
            repeating_value = i

    return miss_value, repeating_value

missing_value, repeating_value = find_missing_and_repeating_number(l)
print("Missing value",missing_value)
print("Repeating value",repeating_value)
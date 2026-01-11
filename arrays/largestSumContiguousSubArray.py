l = [-2,-1,-3,4,-1,2,1,-5,4]

def largest_sub_array(arr:list)->list:
    """It check for the max sum of contiguous sub_array and return max_sum and largest_sub_array"""
    max_sum = arr[0]
    largest_array = arr[0]
    for i in range(1, len(arr)):
        step = i
        for j in range(len(arr)):
            if sum(arr[j:j+step]) > max_sum:
                max_sum = sum(arr[j:j+step])
                largest_array = arr[j:j+step]
    return max_sum, largest_array


max_sum, largest_array = largest_sub_array(l)
print(max_sum)
print(largest_array)
l = [1,2,3,4,5,6,7]
def rotate_array_from_right(arr:list,k:int)->list:
    """It will remove the last element and place it in first place"""
    for i in range(k):
        last_element = arr.pop()
        arr.insert(0,last_element)
    return arr

def rotate_array_from_left(arr:list,k:int)->list:
    """It will remove the first element and place it in last place"""
    for i in range(k):
        first_element = arr.pop(0)
        l.append(first_element)
    return arr

left_arr = rotate_array_from_left(l,3)
print(left_arr)
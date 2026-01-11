l = [1,2,3,4,5,2,3,2,3]

def duplicate_number(arr:list)->int:
    """Checks for duplicate number in list and returns it"""
    repeated=0
    repeated_num = arr[0]
    for i in arr:
        if arr.count(i) > repeated:
            repeated_num = i
            repeated = arr.count(i)
    return repeated_num

repeated_num = duplicate_number(l)
print(repeated_num)
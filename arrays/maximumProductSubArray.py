l = [-1,4,-4,5,-2,-1,-1,-2,-3, 0, 3]


from math import prod
def max_product_sub_array(arr:list)->int:
    """This function check for max_product in contiguous sub_array"""
    max_product = 0
    max_subarray = arr[0]
    for i in range(2,len(arr)):
        for j in range(len(arr)):
            if max_product < prod(arr[j:j+i]):
                max_product = prod(arr[j:j+i])
                max_subarray = arr[j:j+i]
    return max_product, max_subarray

max_prod = max_product_sub_array(l)
print(max_prod)
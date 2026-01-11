l = [[1,3],[2,6],[5,10],[9,18]]

def merge_intervals(arr:list)->list:
    """It checks if there are any intervals which can be merged if yes it will merge and create new interval"""
    arr.sort(key=lambda x:x[0])
    merged = []
    for i in arr:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])
    return merged

merged = merge_intervals(l)
print(merged)
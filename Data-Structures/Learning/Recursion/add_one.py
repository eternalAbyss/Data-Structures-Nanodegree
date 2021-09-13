def add_one(arr):
    if len(arr) == 0:
        return [1]
    else:
        arr[-1] += 1
        if arr[-1] > 9:
            arr[-1] %= 10
            return add_one(arr[:-1]) + [arr[-1]]
        else:
            return arr


print(add_one([1, 9, 9]))

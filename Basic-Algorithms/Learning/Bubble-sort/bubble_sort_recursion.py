def bubble_sort_recursion(array, target, left=0):
    if len(array) == 0:
        return None
    mid = (len(array) - 1) // 2
    if array[mid] == target:
        return mid + left
    elif target > array[mid]:
        return bubble_sort_recursion(array[mid + 1:], target, left + mid + 1)
    else:
        return bubble_sort_recursion(array[:mid], target, left)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 6

testcase = bubble_sort_recursion(arr, num)
print(testcase)


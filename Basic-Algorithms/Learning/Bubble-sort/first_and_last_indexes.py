def first_and_last_index(arr, target):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index

    index = recursive_binary_search(arr, target)
    if index is None:
        return [-1, -1]

    first_index = index
    last_index = index
    while arr[first_index] == target:
        first_index -= 1
        if first_index < 0:
            break

    while arr[last_index] == target:
        last_index += 1
        if last_index >= len(arr):
            break

    return [first_index + 1, last_index - 1]


def recursive_binary_search(arr, target, left=0):
    if len(arr) == 0:
        return None

    mid = (len(arr) - 1) // 2
    mid_ele = arr[mid]

    if mid_ele == target:
        return mid + left
    elif target > mid_ele:
        return recursive_binary_search(arr[mid + 1:], target, mid + left + 1)
    else:
        return recursive_binary_search(arr[:mid], target, left)

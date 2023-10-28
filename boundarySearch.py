def boundary_search_bool(arr: list[bool]) -> int:
    """
        For a boolean array that can be cleanly divided into two completely
        true/false subsets, find the boundary between the true/false subsets.
        Return the index of the boundary.
    """
    boundary_index = -1
    left, right = 0, len(arr) - 1

    if arr[0]:
        condition = lambda x: not x
    else:
        condition = lambda x: x

    while left <= right:
        mid = (left + right) // 2
        if condition(arr[mid]):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


def boundary_search_monotonic(arr: list[int | float], target: int) -> int:
    """
        For a monotonically increasing or decreasing array of numbers, find the
        boundary where the rest of the array is >= or <= a target number.
        Return the index of the boundary.
    """
    boundary_index = -1
    left, right = 0, len(arr) - 1

    if arr[0] < arr[-1]:
        condition = lambda x, y: (x >= y)
    else:
        condition = lambda x, y: (x <= y)

    while left <= right:
        mid = (left + right) // 2
        if condition(arr[mid], target):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


if __name__ == '__main__':
    print("----------------------------------------------------------\n")
    print("Testing boolean boundary search...")
    arr = [False, False, False, True, True, True, True]
    print(arr, "Boundary: {}".format(boundary_search_bool(arr)))
    arr.reverse()
    print(arr, "Boundary: {}".format(boundary_search_bool(arr)))
    print("----------------------------------------------------------\n")

    print("Testing monotonic boundary search...")
    arr = [x for x in range(0, 9)]
    target = 4
    print(arr, "Boundary: {0}, Target: {1}".format(boundary_search_monotonic(arr, target), target))
    arr.reverse()
    target = 7
    print(arr, "Boundary: {0}, Target: {1}".format(boundary_search_monotonic(arr, target), target))
    print("----------------------------------------------------------")

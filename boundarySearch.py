
def boundary_search(arr: list[bool]):
    """
         Find the boundary in an array of boolean values that 
        can be split cleanly between true/false entries. 
    """
    boundary_index = -1
    left, right = 0, len(arr) -1
    
    if arr[0] == False:
        condition =  lambda x : x
    else:
        condition =  lambda x : not x
    
    while left <= right:
        mid = (left + right)//2        
        if condition(arr[mid]):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


if __name__=='__main__':
    arr = [ False, False, False, True, True, True, True]
    arr.reverse()
    print(boundary_search(arr))



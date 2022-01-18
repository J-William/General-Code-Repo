import random   # For building a pseudorandom linked list

# Basic implementation of applying mergesort to a linked list 


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
def buildRandomList (a,b):
    """ Build a pseudorandom linked list for testing. """
    
    length = random.randrange(a,b)
    head = Node(None)
    ptr = head
    
    for _ in range(length):
        ptr.next = Node(random.randrange(100))
        ptr = ptr.next
        
    return head.next
                
                
def printList (head):
    """ Print a linked list in python list format. """
    
    result = []
    
    while head is not None:
        result.append(head.val)
        head = head.next
        
    print(result)


def findMid (head):
    """ Find the middle of a linked list with fast and slow ptr """
    
    sptr = head
    fptr = head.next
    
    while (fptr is not None and fptr.next is not None):
        sptr = sptr.next
        fptr = fptr.next.next
        
    return sptr
    
    
def merge (list1, list2):
    """ Merge subroutine. """
    
    newHead = Node(None)
    temp = newHead
    
    # Comparison sorting
    while (list1 is not None and list2 is not None):
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        
        temp = temp.next
        
    # Append any leftovers
    while (list1 is not None):
        temp.next = list1
        list1 = list1.next
        temp = temp.next
    while (list2 is not None):
        temp.next = list2
        list2 = list2.next
        temp = temp.next
        
    return newHead.next
            
    
def mergeSort (head):
    """ Merge sort a  linked list. """
    
    # Base Case
    if head.next == None:
        return head
    
    # Find the midpoint
    mid = findMid(head)

    # Divide into subarrays
    L = head
    M = mid.next
    mid.next = None

    # Recursive sort
    L = mergeSort(L)
    M = mergeSort(M)

    # Combine the subarrays
    return merge(L, M)   
    
    
    
def main():
    ptr = buildRandomList(5,10)
    print('Pre sort:')
    printList(ptr)
    ptr = mergeSort(ptr)
    print('Post sort:')
    printList(ptr)
    
    
    

if __name__ == '__main__':
    main()

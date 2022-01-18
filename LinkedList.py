# A linked list implementation with several utility methods 

class LinkedList:
    
    class Node:    
        def __init__ (self, x):
            self.val = x
            self.next = None
        
        
    def __init__ (self, x):
        self.head = self.Node(x)
        
        
    def printList (self):
        ptr = self.head
        theList = []
        while (ptr != None):
            theList.append(ptr.val)
            ptr = ptr.next
        print(theList)
    
    
    def add (self, x):
        """ Add a new element to the end of the list. """
        ptr = self.head
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = self.Node(x)
    
    
    def pop (self, y):
        """ Return the given index from the list; deleting from the list. """
        ptr = self.head
        
        if y == 1:
            result = head.val
            head = head.next
            return result
        
        # Iterate i-1 times to arrive at the element before the insertion point
        for _ in range(y-2):
            ptr = ptr.next
        
        result = ptr.next.val
        ptr.next = ptr.next.next           
        
        return result
        
        
    def insert (self, x, y):
        """ Insert a value at a given index. """
        ptr = self.head
        if y == 1:
            ptr = self.Node(x)
            ptr.next = head
            head = ptr
            
        else:
            for _ in range(y-2):
                ptr = ptr.next
            
            newNode = self.Node(x)
            newNode.next = ptr.next
            ptr.next = newNode
    
    
    def search (self, x):
        """ Return the first index of an element if it is present in the list. """
        current = self.head
        i = 0
        
        while (current != None):
            i += 1
            
            if current.val == x:
                return i
            else:
                current = current.next
            
    
    def remove (self, x):
        """ Find and remove an element from the list """
        index = self.search(x)
        self.pop(index)
        
        
    def sort (self):
        """ Bubble sort the list. """
        current = self.head
        fptr = self.Node(None)
        
        # Outer access iteration
        while (current != None):
            # fptr starts at the next element past current
            fptr = current.next
            
            # fptr moves up the list comparing with current and swapping 
            # if a smaller value is found
            while (fptr != None):
                if (current.val > fptr.val):
                    current.val, fptr.val = fptr.val, current.val
                fptr = fptr.next
            
            current = current.next

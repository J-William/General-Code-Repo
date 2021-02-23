"""Problem setup for the 8-block toy problem"""

class Problem():
    def __init__(self, i):
        self.InitialState = i

    def Actions(self, s):             # returns available actions in s
        a = { 0 : ["Right", "Down"], 1 : ["Left", "Right", "Down"], 2: ["Left", "Down"],
                3: ["Up", "Right", "Down"], 4: ["Up","Left", "Right", "Down"], 5: ["Up", "Left", "Down"],
                    6: ["Up", "Right"], 7: ["Up","Left", "Right"], 8: ["Up","Left"] }

        return a[s.index(0)]




    def Result(self, s, a):           # returns results of action in s
        
        def Up(s):      # Up returns a new state after an Up action
            blank = s.index(0)
            npos = blank - 3
            s[blank] = s[npos]
            s[npos] = 0
            return s

        def Down(s):    # Down action
            blank = s.index(0)
            npos = blank + 3
            s[blank] = s[npos]
            s[npos] = 0
            return s

        def Left(s):    # Left action
            blank = s.index(0)
            npos = blank - 1
            s[blank] = s[npos]
            s[npos] = 0
            return s

        def Right(s):    # Right action
            blank = s.index(0)
            npos = blank + 1
            s[blank] = s[npos]
            s[npos] = 0
            return s

        """ Control block for which action is executed based on arg """
        
        if a == 'Up':
            return Up(s)
        elif a == 'Down':
            return Down(s)
        elif a == 'Left':
            return Left(s)
        elif a == 'Right':
            return Right(s)

    def GoalTest(self, s):
        if s == [ 1,2,3,4,5,6,7,8,0 ]:
            return True
        else:
            return False

    def Mdistance(self, s):           # Calculates the Manhattan distance from s to goal state
        cost = 0
        
        # Mdistance for 1-7
        for value in range(1,9):
            distance = abs((value -1)-s.index(value))
            if distance >= 6:
                cost += 2
                cost += distance%3
            elif distance >= 3:
                cost += 1
                cost += distance%3
            else:
                cost += distance
            
                
        # Mdistance for the blank
        distance = abs(8-s.index(0))
        if distance >= 6:
                cost += (2+(distance%3))
        elif distance >= 3:
                cost += (1+(distance%3))
        else:
                cost += distance

        return cost

            
        

class Node():
    def __init__(self):
        self.State = None
        self.Parent = None
        self.Action = None      # action that created the node
        self.G = None           # the path cost to this node from initial
        self.H = None          # the m-distance to G from this state

class Frontier():
    def __init__(self):
        self.front = {}

    # Adds an element f=h+g, node
    def add(self, f, n):
        self.front[f] = n

    # Searches for a state within the frontier's nodes 
    def search(self, s):
        for node in self.front.values():
            if node.State == s:
                return True
        return False


    # Pops the element with the lowest key 
    def pop(self):
        key = min(self.front.keys()) # find min key
        entry = self.front[key]
        del self.front[key]          # delete the entry
        return entry                    # return value for key

    # Pop the element with the given state
    def get(self, s):                   
        for item in self.front.items():
            if item[1].State == s:
                key = item[0]
        entry = self.front[key]
        del self.front[key]        
        return [key, entry]

class Explored():
    def __init__(self):
        self.set = []
    def search(self, s):
        for state in self.set:
            if s == state:
                return True
        return False
    def add(self, s):
        self.set.append(s)


def Solution(node):
    solution = []
    
    while node.Parent != None:
        solution.append(node.Action)
        node = node.Parent

    return solution
    

def ChildNode(problem, parent, action):
    new_node = Node()
    new_node.State = problem.Result(parent.State, action)
    new_node.Parent = parent
    new_node.Action = action
    new_node.G = (parent.G + 1)
    new_node.H = problem.Mdistance(new_node.State)
    return new_node







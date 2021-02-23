import SetupDraft as E

""" AI homework assignment 8-Block Algorithm """


problem = E.Problem([2,3,6,1,4,8,7,0,5])


def AstarSearch(problem):
    
    node = E.Node()
    node.State = problem.InitialState
    node.G = 0
    node.H = problem.Mdistance(node.State)

    frontier = E.Frontier()             # Create a priority queue and add root node
    frontier.add(node.G+node.H, node)

    explored = E.Explored()

    while (True):
        if not frontier:                    # Empty frontier is fail state
            return "Faiure"
        
        node = frontier.pop()               # Choose lowest F node                 
        
        if(problem.GoalTest(node.State)):   # Test for goal
            return Solution(node)

        explored.add(node.State)         # Add state to explored set
        
        for action in problem.Actions(node.State):
            
            child = E.ChildNode(problem, node, action)      # for each action possible from s create a child

            if (explored.search(child.State) & frontier.search(child.State)) == False:      # if the child is not in explored or frontier add to frontier
                frontier.add(child.G+child.H, child)
            elif frontier.search(child.State):                                              # if it is in frontier and lower f replace with the child
                frontier_node = frontier.get(child.State)
                if frontier_node[0] > (child.G+child.H):
                    frontier.add(child.G+child.H, child)
                else:                                                                       # else do nothing
                    frontier.add(frontier_node[0], frontier_node[1])
                    
                            
                        
                

r = AstarSearch(problem)


               




                            
                    
                
                
            


    

    



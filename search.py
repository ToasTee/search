# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    fringe.push((problem.getStartState(), [], [])) #Fringe (Nodes, Actions, Visited Nodes)
    
    while not fringe.isEmpty():                                     #Loop Do
        node, act, visited = fringe.pop()                               #Node remove front
        if problem.isGoalState(node):                                   #If node is goal
            return path                                                     #Return path until goal
        for succ, dir, visit in problem.getSuccessors(node):            #If node is not goal:
            if succ not in visited:                                         #search each successor, if it is not already visited
                fringe.push((succ, act + [dir], visited + [node]))              #add succ to search stack
                path = act + [dir]                                              #record path taken
    return []                                                       #If fringe is empty, return fail


    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Since we search the shallowest nodes, we can use the queue function to add to the queue the nodes adjacent to our initial node, and add new nodes to the back of the queue.
    fringe = util.Queue()
    fringe.push((problem.getStartState(), [], [])) #Fringe and first node input (Nodes, Actions, Costs)
    visited = [] #Collection of visited nodes
    
    while not fringe.isEmpty(): #Looper
        node, act, cost = fringe.pop() #Remove front node, path to node, cost to node
        if not node in visited:
            visited.append(node) #add node to visited
            if problem.isGoalState(node): #Check if node is goal
                return act #return path to node
            for succ, dir, costs in problem.getSuccessors(node): #if node is not goal
                fringe.push((succ, act + [dir], cost + [costs])) #add successors to queue

    
    
    return [] #Dead end
    
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Sicne we have to prioritize the node path with the least costs first, a priority queue is probably the way to go.
    
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(),[],0),0) #PQ (start, priority 0)
    visited=[]
    
    while not fringe.isEmpty():
        node, act, cost = fringe.pop()
    
        if not node in visited:
            visited.append(node)

            if problem.isGoalState(node):
                return act
            for succ, dir, costs in problem.getSuccessors(node):
                    fringe.push((succ, act + [dir], cost + costs), cost +costs)
                
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    fringe.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    visited = []

    while not fringe.isEmpty():
        node, act,cost = fringe.pop()
        
        if not node in visited:
            visited.append(node)
            
            if problem.isGoalState(node):
                return act
            
            for succ, dir, costs in problem.getSuccessors(node):
                fringe.push((succ, act+[dir], cost + costs), cost + costs + heuristic(succ, problem))
    
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

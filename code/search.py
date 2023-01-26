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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    """
    # Frontier, stack (LIFO), with the nodes to explore associated with actions needed to reach that node from intial node.
    frontier = util.Stack()
    exploredNodes = []
    nodeActionFromStartState = []
    # Initial position (node)
    startNode = problem.getStartState()

    frontier.push((startNode, []))    
    while not frontier.isEmpty():
        node, nodeActionFromStartState = frontier.pop()
        if node not in exploredNodes:
            exploredNodes.append(node)
            # If goal node is encourted, research algorithm is stopped and actions since intial node are sent
            if problem.isGoalState(node):
                return nodeActionFromStartState
            # Else add successor nodes and their actions to frontier.
            else:
                successors = problem.getSuccessors(node)
                for successorNode, sucessorAction, sucessorStepCost in successors:
                    frontier.push((successorNode, nodeActionFromStartState+[sucessorAction]))
    return nodeActionFromStartState


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    """
    # Frontier, queue (FIFO), with the nodes to explore associated with actions needed to reach that node from intial node.
    frontier = util.Queue()
    exploredNodes = []
    # Initial position (node)
    startNode = problem.getStartState()
    nodeActionFromStartState = []
    
    # Add root node in frontier
    frontier.push((startNode, []))
    while not frontier.isEmpty():
        node, nodeActionFromStartState = frontier.pop()
        if node not in exploredNodes:
            exploredNodes.append(node)\
            # If goal node is encourted, research algorithm is stopped and actions since intial node are sent
            if problem.isGoalState(node):
                return nodeActionFromStartState
            # Else add successor nodes and their actions to frontier.
            else:
                successors = problem.getSuccessors(node)
                for successorNode, sucessorAction, sucessorStepCost in successors:
                    frontier.push((successorNode, nodeActionFromStartState+[sucessorAction]))
    return nodeActionFromStartState



def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    """
    # Frontier, priority queue, with the nodes to explore associated with actions needed to reach that node from intial node.
    frontier = util.PriorityQueue()
    exploredNodes = []
    # Initial position (node)
    startNode = problem.getStartState()
    nodeActionFromStartState = []

    # Add root node in frontier with 0 as priority and 0 as cost
    frontier.update((startNode, [], 0),0)
    while not frontier.isEmpty():
        node, nodeActionFromStartState, costFromStartState = frontier.pop()
        if node not in exploredNodes:
            exploredNodes.append(node)
            if problem.isGoalState(node):
                return nodeActionFromStartState
            else:
                successors = problem.getSuccessors(node)
                for successorNode, sucessorAction, sucessorStepCost in successors:
                    frontier.update((successorNode, nodeActionFromStartState+[sucessorAction], sucessorStepCost + costFromStartState),sucessorStepCost + costFromStartState)
    return nodeActionFromStartState


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    """
    # Frontier, priority queue, with the nodes to explore associated with actions needed to reach that node from intial node.
    frontier = util.PriorityQueue()
    exploredNodes = []
    # Initial position (node)
    startNode = problem.getStartState()
    nodeActionFromStartState = []
    #heuristic value
    heuristicValue = 0
    if heuristic(startNode,problem) is not None:
        heuristicValue = heuristic(startNode,problem)
    evaluationFunction = 0 + heuristicValue

    frontier.update((startNode, [], 0),evaluationFunction)
    while not frontier.isEmpty():
        node, nodeActionFromStartState, costFromStartState = frontier.pop()
        if node not in exploredNodes:
            exploredNodes.append(node)
            if problem.isGoalState(node):
                return nodeActionFromStartState
            else:
                successors = problem.getSuccessors(node)
                for successorNode, sucessorAction, sucessorStepCost in successors:
                    if heuristic(successorNode,problem) is not None:
                        heuristicValue = heuristic(successorNode,problem)
                    evaluationFunction = sucessorStepCost + costFromStartState + heuristicValue
                    frontier.update((successorNode, nodeActionFromStartState+[sucessorAction], sucessorStepCost + costFromStartState),evaluationFunction)
    return nodeActionFromStartState



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

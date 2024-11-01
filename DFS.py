import copy
from collections import deque
from classes import Node, directions

def dfs(originalBoard, originalPlayer, originalGoals):
    board = copy.deepcopy(originalBoard)
    goals = copy.deepcopy(originalGoals)
    player = originalPlayer
    
    visited = set()
    startNode = Node(board, player, goals, "", 0)
    stack = deque()

    stack.append(startNode)
    visited.add(startNode.ID)
    # print(board)
    
    while stack:
        node = stack.pop()
        
        if (node.isGoalState()): break
        if (node.isDeadlocked()): continue
        
        for dir in directions:
            if (node.canMove(dir)):
                newNode = node.move(dir)
                if (newNode.ID not in visited):
                    stack.append(newNode)
                    visited.add(newNode.ID)
    
    path = node.path
    print("\nResult path: ", path)
    
    
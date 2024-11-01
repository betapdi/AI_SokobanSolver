import copy
import heapq
from classes import Node, directions, Pair

def manhattanDistance(node):
    totalCost = 0
    targets = list()
    boxPositions = list()
    
    for goal in node.goals:
        if (node.board[goal.x][goal.y].type != '$'):
            targets.append(goal)
    
    for r in range(len(node.board)):
        for c in range(len(node.board[r])):
            if (node.board[r][c].type == '$') and (Pair(r, c) not in node.goals):
                boxPositions.append(Pair(r, c))
    
    for box in boxPositions:
        distance = []
        
        for target in targets:
            distance.append((abs(box.x - target.x) + abs(box.y - target.y)) * node.board[box.x][box.y].weight)
        
        totalCost += min(distance)
    
    return totalCost

def AStarAlgorithm(originalBoard, originalPlayer, originalGoals):
    board = copy.deepcopy(originalBoard)
    goals = copy.deepcopy(originalGoals)
    player = originalPlayer
    
    visited = set()
    startNode = Node(board, player, goals, "", 0)
    pq = []
    heapq.heappush(pq, startNode)
    
    while pq:
        heapq.heapify(pq)
        node = heapq.heappop(pq)
        
        if (node.isGoalState()): break
        
        
        if (node.ID in visited): continue
        visited.add(node.ID)
        
        if (node.isDeadlocked()): continue
        
        for dir in directions:
            if (node.canMove(dir)):
                newNode = node.move(dir)
                newNode.heuristicCost = manhattanDistance(newNode)
                
                if (newNode.ID not in visited):
                    heapq.heappush(pq, newNode)
    
    path = node.path
    print("\nResult path: ", path)
    
    
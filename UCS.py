import copy
import heapq
from classes import Node, directions

def uniformCostSearch(originalBoard, originalPlayer, originalGoals):
    board = copy.deepcopy(originalBoard)
    goals = copy.deepcopy(originalGoals)
    player = originalPlayer
    
    visited = set()
    startNode = Node(board, player, goals, "", 0)
    pq = []
    heapq.heappush(pq, startNode)
    cnt = 0
    
    # print(board)
    
    # for r in range(len(board)):
    #     for c in range(len(board[r])):
    #         print(board[r][c].type, end='')
    #     print()
    
    while pq:
        heapq.heapify(pq)
        node = heapq.heappop(pq)
        
        if (node.isGoalState()): break
        
        if (node.ID in visited): continue
        visited.add(node.ID)
        
        if (node.isDeadlocked()): continue
        
        # print(node.ID)
        
        # for r in range(len(node.board)):
        #     for c in range(len(node.board[r])):
        #         print(board[r][c].type, end='')
        #     print()
        
        for dir in directions:
            if (node.canMove(dir)):
                newNode = node.move(dir)
                if (newNode.ID not in visited):
                    heapq.heappush(pq, newNode)
    
    path = node.path
    print("\nResult path: ", path)
    
    
import copy
import queue
from classes import Node, directions

def bfs(originalBoard, originalPlayer, originalGoals):
    board = copy.deepcopy(originalBoard)
    goals = copy.deepcopy(originalGoals)
    player = originalPlayer
    
    visited = set()
    startNode = Node(board, player, goals, "", 0)
    q = queue.Queue()

    q.put(startNode)  
    visited.add(startNode.ID)  
    # print(board)
    
    # for r in range(len(board)):
    #     for c in range(len(board[r])):
    #         print(board[r][c].type, end='')
    #     print()
    
    while not q.empty():
        node = q.get()
        
        if (node.isGoalState()): break
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
                    q.put(newNode)
                    visited.add(newNode.ID)
    
    path = node.path
    print("\nResult path: ", path)
    
    
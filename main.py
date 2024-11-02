import os
from inOut import readFile, writeFile
from classes import Pair, Cell

from UCS import uniformCostSearch
from AStar import AStarAlgorithm
from BFS import bfs
from DFS import dfs

def dataProcessing(weights, matrix):
    stones = []
    goals = list()
    board = []
    index = 0
    player = Pair(0, 0)
    
    for i in range(len(matrix)):
        board.append([])
        
        for j in range(len(matrix[i])):
            board[i].append(Cell(matrix[i][j], 0))
            
            if matrix[i][j] == '$':
                stones.append({"weight": weights[index], "position": Pair(i, j)})
                board[i][j].weight = weights[index]
                index += 1
            
            elif matrix[i][j] == '@':
                player = Pair(i, j)
                board[i][j].type = ' '
                
            elif matrix[i][j] == '.':
                goals.append(Pair(i, j))
                board[i][j].type = ' '
                
            elif matrix[i][j] == '*':
                stones.append({"weight": weights[index], "position": Pair(i, j)})
                board[i][j].weight = weights[index]
                index += 1
                goals.append(Pair(i, j))
                
            elif matrix[i][j] == '+': 
                board[i][j].type =  ' '
                goals.append(Pair(i, j))
                player = Pair(i, j)
                
    return stones, player, goals, board

filePath = "input.txt"
weights, matrix = readFile(filePath)

# print("\nWeights: ", weights)
# print("\nMatrix: ", matrix)

stones, player, goals, board = dataProcessing(weights, matrix)
# print("\nStones: ", stones)
# print("\nBoard: ", board)

# uniformCostSearch(board, player, goals)
path, cost, time, memoryUsed, cntNode = AStarAlgorithm(board, player, goals)
# bfs(board, player, goals)
# dfs(board, player, goals)

writeFile("output.txt", "A_Star", path, cost, time, memoryUsed, cntNode)



import os

def readFile(path):
    with open(path, "r") as file:
        lines = file.readlines()
        
    weights = list(map(int, lines[0].split()))
    matrix = [list(lines[x].rstrip('\n')) for x in range(1, len(lines))]
    
    return weights, matrix
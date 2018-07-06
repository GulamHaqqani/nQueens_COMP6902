import numpy as np
import csv
import os
import random
import pandas as pd

n = int(input("Please enter the board size "))
k = int(input("Please enter the number of queens to be randomly placed on the board  "))
board = np.zeros((n, n), dtype=int)

for c in range(k):
    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    board[i][j] = 1

def checkRowConflict(row, col):
    if(col<n-1):
        board[row][col+1]=0
    col = col +1
    if(col<n-1):
        checkRowConflict(row, col)

def checkColConflict(row, col):
    if(row<n-1):
        board[row+1][col]=0
    row = row + 1
    if(row<n-1):
        checkColConflict(row, col)

def checkDiagConflict(row, col):
    if(row<n-1 & col<n-1):
        board[row+1][col+1]=0
        board[row-1][col-1]=0
        board[row+1][col-1]=0
        board[row-1][col+1]=0
    row = row + 1
    col = col + 1
    if(row<n & col<n):
        checkDiagConflict(row, col)
    if(row == n-1 | col == n):
        quit()


def writetoCSV(row, col):
    filepath = os.getcwd()
    data = row, col
    with open("result.csv", "a") as csv_file:
        csv_data = csv.writer(csv_file)
        csv_data.writerow(data)





for i in range(n):
    for j in range(n):
        if(board[i][j]==1):
            row = i
            col = j
            checkRowConflict(row, col)
            checkColConflict(row, col)
            checkDiagConflict(row, col)

print(board)

print("Writing the result to the CSV file")
for i in range(n):
    for j in range(n):
        if(board[i][j]==1):
            writetoCSV(i, j)


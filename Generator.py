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


    
with open("result.csv", "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = ["rows", "columns"])
        writer.writeheader()
        
def writetoCSV(row, col):
    filepath = os.getcwd()
    data = row, col
    with open("result.csv", "a") as csv_file:
        csv_data = csv.writer(csv_file)
        csv_data.writerow(data)


print("Writing the result to the CSV file")
for i in range(n):
    for j in range(n):
        if(board[i][j]==1):
            writetoCSV(i, j)

print(board)

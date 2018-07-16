
# coding: utf-8

# In[ ]:


import numpy as np
import csv
import os
import sys
import pandas as pd

n = int(input("Enter the number of Queens"))
board = np.zeros((n,n), dtype=int)

df = pd.read_csv('result.csv', usecols=None)

row = df['rows'].values.tolist()
col = df['columns'].values.tolist()

for i in range(len(row)):
    for j in range(len(col)):
        temp1 = row[j]
        temp2 = col[j]
        board[temp1][temp2] = 1

list = [[]]
cnf = []

varList = []
for i in range(1, (n*n)+1):
    varList.append(i)


for i in range(1, n):
    list.append([])

for i in range(n):
    for j in range(n):
        count = (i*n) + j
        for k in range(1):
            list[i].append(varList[count])

for i in range(n):
    for j in range(n):
        p = i
        q = j
        if(board[p][q] == 1):
            if(p==0):
                if(q == 0):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 1):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 2):
                    cnf.append(list[p][q])
                    cnf.append(0)
            elif(p==1):
                if(q == 0):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 1):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 2):
                    cnf.append(list[p][q])
                    cnf.append(0)
            elif(p==2):
                if(q == 0):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 1):
                    cnf.append(list[p][q])
                    cnf.append(0)
                if(q == 2):
                    cnf.append(list[p][q])
                    cnf.append(0)
for i in range(n):
    for j in range(n):
        if(board[i][j] == 1):
            #Front
            #Run Row Check
            p=i+1;
            q=j+1;
            print(board)
            while(p<=n-1):
                if(board[i][j] == board[p][j]):
                    print("Row CNF")
                    print(i,j,p,j)
                    temp0= list[i][j] * -1
                    cnf.append(temp0)
                    cnf.append(0)
                    print(p, j)
                    temp1= list[p][j] * -1
                    cnf.append(temp1)
                    cnf.append(0)
                p=p+1
            #Run Column Check
            while(q<=n-1):
                if(board[i][j] == board[i][q]):
                    print("Column CNF")
                    print(i,j,i,q+1)
                    temp0= list[i][j] * -1
                    cnf.append(temp0)
                    cnf.append(0)
                    temp1= list[i][q] * -1
                    cnf.append(temp1)
                    cnf.append(0)
                q=q+1
            #Run Diagonal Check
            while(p<=n-1):
                while(q<=n-1):
                    if(board[i][j] == board[p][q]):
                        print("Diagonal CNF")
                        temp0= list[i][j] * -1
                        print(i,j,p+1,q+1)
                        cnf.append(temp0)
                        cnf.append(0)
                        temp1= list[p][q] * -1
                        cnf.append(temp1)
                        cnf.append(0)
                    q=q+1
                p=p+1

out = ""
out = out + "p" + " " + "cnf" + " " + str(len(varList)) + " " + str(len(cnf)) + "\n"
print(cnf)

for i in range(0, len(cnf), 2):
    out += str(cnf[i]) + " " + str(cnf[i+1]) + "\n"

f = open("nQueensCNF.cnf", "w")
f.write(out)
f.close()

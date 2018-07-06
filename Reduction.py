#!/usr/bin/python3
'''
	CNF generator for n queens problem
'''

class Queens:

	def __init__(this, totalQueens):
		this.n = totalQueens
		stand = 1
		this.cnf = list();
		this.chess_board = [[0 for x in range(this.n)] for y in range(this.n)]
		for i in range(0,this.n):
			for j in range(0,this.n):
				this.chess_board[i][j] = stand
				stand += 1

	def addToCNF(this, literals, insert=False):
		if insert:
			this.cnf.append(literals)
		# this.cnf.append(literals)
		n = len(literals)
		CNFList = list();
		for j in range(0,n-1):
			for k in range(j+1,n):
				CNFList.append(-literals[j])
				CNFList.append(-literals[k])
				this.cnf.append(CNFList)
				CNFList = []

	def saveFile(this):
		endOfFormulae = "0"
		out = "p cnf " + str(this.n*this.n) + " " + str(len(this.cnf)) + "\n"
		for i in range(0,len(this.cnf)):
			for j in range(0,len(this.cnf[i])):
				out += str(this.cnf[i][j]) + " "
			out += endOfFormulae + "\n"

		f = open('nQueens.cnf', 'w')
		f.write(out)

	def main(this):
		vRows = list();
		vColumns = list();
		Diag1 = list();
		Diag2 = list();
		Diag3 = list();
		Diag4 = list();

		# CNF for rows
		for i in range(0,this.n):
			for j in range(0,this.n):
				vRows.append(this.chess_board[i][j])
			this.addToCNF(vRows, True)
			vRows = []

		# CNF for collumns
		for i in range(0,this.n):
			for j in range(0,this.n):
				vColumns.append(this.chess_board[j][i])
			this.addToCNF(vColumns, True)
			vColumns = []

		# CNF for diagonals
		for i in range(0,this.n-1):
			for j in range(0,this.n-i):
				Diag1.append(this.chess_board[i][i+j])
			this.addToCNF(Diag1)
			Diag1 = []

		for i in range(0,this.n-1):
			for j in range(0,this.n-i):
				Diag2.append(this.chess_board[j][this.n-1-(i+j)])
			this.addToCNF(Diag2)
			Diag2 = []

		for i in range(1,this.n-1):
			for j in range(0,this.n-i):
				Diag3.append(this.chess_board[j+i][i])
			this.addToCNF(Diag3)
			Diag3 = []

		for i in range(1,this.n-1):
			for j in range(0,this.n-i):
				Diag4.append(this.chess_board[j+i][this.n-1-j])
			this.addToCNF(Diag4)
			Diag4 = []

totalQueens = int(input("Please enter the number of Queens ?\n"))
if totalQueens > 3:
	myQueens = Queens(totalQueens)
	myQueens.main()
	myQueens.saveFile()
	print("NQueens.cnf has been generated")
else:
	print("Eight queens puzzle is solvable only for n > 3")

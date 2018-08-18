import numpy as np
from pprint import pprint as pp

sudoku = [
[[0],[4],[3],[2],[6],[0],[0],[0],[0]],
[[0],[0],[6],[0],[0],[0],[0],[0],[3]],
[[0],[8],[9],[1],[0],[5],[0],[0],[0]],
[[0],[3],[0],[6],[0],[0],[0],[0],[4]],
[[4],[7],[0],[0],[1],[0],[0],[3],[8]],
[[8],[0],[0],[0],[0],[4],[0],[7],[0]],
[[0],[0],[0],[7],[0],[6],[1],[8],[0]],
[[1],[0],[0],[0],[0],[0],[9],[0],[0]],
[[0],[0],[0],[0],[9],[1],[3],[2],[0]]
]

solution = sudoku

for row in range(9):
	for col in range(9):
		if sudoku[row][col][0]==0:
			solution[row][col]=range(1,10)

def getBox(i,j):
	boxis = [
	i, i, i,
	i+1, i+1, i+1,
	i+2, i+2, i+2]

	boxjs = [
	j, j+1, j+2,
	j, j+1, j+2,
	j, j+1, j+2]

	return boxis, boxjs

def findBox(row,col):
	for i in range(3):
		if row in range(3*i,3*i+3):
			boxi = 3*i

		if col in range(3*i,3*i+3):
			boxj = 3*i

	return boxi, boxj

def eliminate(n,row,col):
	# Reduce row and column
	for i in range(9):
		try:
			if len(solution[row][i])>1: solution[row][i].remove(n)
		except: pass

		try:
			if len(solution[i][col])>1: solution[i][col].remove(n)
		except: pass

	# Reduce the box
	boxi, boxj = findBox(row,col)
	boxis, boxjs = getBox(boxi,boxj)

	for i in range(9):
		try:
			if len(solution[boxis[i]][boxjs[i]])>1: solution[boxis[i]][boxjs[i]].remove(n)
		except: pass

	return None

def showBoard(s):
	for row in range(9):
		print '\n'
		for col in range(9):
			print s[row][col],'\t',
	print '\n'
	return None

iter = 1
rOld = 9*9

while 1:
	for row in range(9):
		for col in range(9):
			try:
				if len(solution[row][col])==1: eliminate(solution[row][col][0],row,col)
			except: pass

	r = 0
	for row in range(9):
		for col in range(9):
			if len(solution[row][col])>1: r=r+1

	print "\n\nIteration : ",iter," Remaining Entries : ",r
	iter=iter+1

	showBoard(solution)

	if not r:
		break

	if r==rOld:
		break
	else:
		rOld=r
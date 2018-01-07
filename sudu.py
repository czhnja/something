# -*- coding: utf8 -*-
# author = ZhnJa
# Depth First Search,solve SUDU

problem = [
		[0,1,0,0,0,6,2,0,0],
		[0,0,0,5,3,0,9,0,8],
		[6,9,0,2,4,0,0,0,0],
		[7,0,0,0,0,0,3,9,0],
		[0,3,5,0,6,0,8,4,0],
		[0,8,4,0,0,0,0,0,7],
		[0,0,0,0,5,4,0,3,1],
		[4,0,6,0,8,3,0,0,0],
		[0,0,1,9,0,0,0,8,0]
]
problem1 = [
		[0,1,3,8,9,6,2,7,4],
		[2,0,7,5,3,1,9,6,8],
		[6,9,8,2,4,7,1,5,3],
		[7,6,2,4,1,8,3,9,5],
		[1,3,5,7,6,9,8,4,2],
		[9,8,4,3,2,5,6,1,7],
		[8,2,9,6,5,4,7,3,1],
		[4,7,6,1,8,3,5,2,9],
		[3,5,1,9,7,2,4,8,6]
]
ans = [
		[5,1,3,8,9,6,2,7,4],
		[2,4,7,5,3,1,9,6,8],
		[6,9,8,2,4,7,1,5,3],
		[7,6,2,4,1,8,3,9,5],
		[1,3,5,7,6,9,8,4,2],
		[9,8,4,3,2,5,6,1,7],
		[8,2,9,6,5,4,7,3,1],
		[4,7,6,1,8,3,5,2,9],
		[3,5,1,9,7,2,4,8,6]
]

#生成列
def columns(temp):
	t=[[],[],[],[],[],[],[],[],[]]
	for i in range(9):
		for j in range(9):
			t[i].append(temp[j][i])
	return t
#生成9个格子
def blocks(temp):
	t=[[],[],[],[],[],[],[],[],[]]
	for k in range(3):
		for i in range(3):
			for j in range(9):
				t[k*3+i/3+j/3].append(temp[k*3+i][j])
	print t


def dfs_sudoku(problem):


	temp = problem#中间处理的状态

	search(0,0,problem)

def search(x,y):
	global p
	global step
	global temp_p
	step = step +1
	if is_complete(temp_p):
		if is_allright(temp_p):
			print temp_p
			return
		return
	while len(p[x*9+y]) != 0:	
		if temp_p[x][y] == 0:
			temp_p[x][y] = p[x*9+y].pop()
		nx,ny = get_next(temp_p)
		print step
		print temp_p
		print p[0]
		print p[10]
		search(nx,ny)
		temp_p[nx][ny] = 0	


def get_next(temp):
	for i in range(9):
		for j in range(9):
			if temp[i][j] == 0:
				return i,j
	return 9,9
def get_possible(temp):
	global p
	for i in range(9):
		for j in range(9):
			if temp[i][j] in p[i*9+j]:
				p[i*9+j].remove(temp[i][j])
	# t = transpose(temp)
	# for i in range(9):
	# 	for j in range(9):
	# 		if temp[i][j] in p[j*9+i]:
	# 			p[j*9+i].remove(temp[i][j])


#按行检查
def is_right(temp):
	count_x = 0
	count_y = 0
	for i in range(9):
		count_x = count_x + 1
		count_y = 0
		for j in range(9):
			if j+1 in temp[i]:
				count_y = count_y + 1
			else:
				#print "Wrong in ["+str(i)+str(j)+"]"
				return False
	return True

#转置，将行与列对换
def transpose(temp):
	t=[[],[],[],[],[],[],[],[],[]]
	for i in range(9):
		for j in range(9):
			t[i].append(temp[j][i])
	return t

#检查是否完成
#先按行检查再按列
def is_allright(temp):
	if is_right(temp):
		if is_right(transpose(temp)):
			return True
		else:
			return False
	else:
		return False

#是否填写写成
def is_complete(temp):
	for i in range(9):
		for j in range(9):
			if temp[i][j]== 0:
				return False
	return True

if __name__ == "__main__":
	n=0
	step = 0
	p = [[1,2,3,4,5,6,7,8,9] for x in range(81)]
	temp_p = problem1
	search(0,0)

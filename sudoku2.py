# -*- coding: utf8 -*-
# author = ZhnJa
# Updated at 20170213
# Depth First Search,solve sudoku
import datetime

p0210 = [
		[0,1,0,0,0,6,2,0,0],
		[0,0,0,5,3,0,9,0,8],
		[6,9,0,2,4,0,0,0,0],
		[7,0,0,0,0,0,3,9,0],
		[0,3,5,0,6,0,8,4,0],
		[0,8,4,0,0,0,0,0,7],
		[0,0,0,0,5,4,0,3,1],
		[4,0,6,0,8,3,0,0,0],
		[0,0,1,9,0,0,0,8,0]]

p0213 = [[0,0,0,8,9,5,7,0,0],
		 [0,0,0,0,0,6,8,0,0],
		 [0,0,0,0,0,0,0,5,0],
		 [6,7,0,0,0,0,0,0,8],
		 [0,9,0,5,0,8,0,4,0],
		 [8,0,0,0,0,0,0,3,9],
		 [0,4,0,0,0,0,0,0,0],
		 [0,0,3,6,0,0,0,0,0],
		 [0,0,6,7,2,1,0,0,0]]

def get_next(x,y,temp):
	for i in range(0,9):
		for j in range(0,9):
			if temp[i][j] == 0:
				return i,j
	return -1,-1

def get_blocks(temp):
	blocks = [ [] for n in range(9)]
	for i in range(9):
		for j in range(9):
			blocks[(i/3)*3+j/3].append(temp[i][j])
	return blocks

def check(x,y,num,temp):
	#按行检查
	if num in temp[x]:
		return False
	#按列检查
	for i in range(9):
		if num == temp[i][y]:
			return False
	#按格检查
	blocks = get_blocks(temp)
	if num in blocks[(x/3)*3+y/3]:
		return False
	return True

#回溯递归求解
def search(x,y,temp):
	if temp[x][y] == 0:
		for num in range(1,10):
			if check(x,y,num,temp):
				temp[x][y] = num
				nx,ny = get_next(x,y,temp)
				if nx == -1:
					return True
				else:
					end = search(nx,ny,temp)
					if not end:
						temp[x][y] = 0
					else:
						return True
	else:
		nx,ny = get_next(x,y,temp)
		search(nx,ny,temp)
	return

#传入9*9的列表
#包含计算时间
def solve(temp):
	begin_time = datetime.datetime.now()
	search(0,0,temp)
	end_time = datetime.datetime.now()
	for i in range(9):
		print temp[i]
	print 'Using Time:',end_time-begin_time
	return temp

if __name__ == "__main__":
	solve(p0213)
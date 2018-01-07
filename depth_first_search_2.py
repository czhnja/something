# -*- coding: utf8 -*-
# author = ZhnJa
# Depth First Search,Page87

def dfs(x,y,step):
	if x==p and y==q:
		global minstep
		if minstep > step:
			minstep = step
			print minstep
			for i in range(0,5):
				for j in range(0,4):
					if book[i][j] == 1:
						print i,j
		return
	for k in range(4):
		tx = x + move[k][0]
		ty = y + move[k][1]
		if tx<0 or tx>=boderx or ty<0 or ty>=bodery:
			continue
		if mapblock[tx][ty] == 0 and book[tx][ty] == 0:
			book[tx][ty] = 1
			dfs(tx,ty,step+1)
			book[tx][ty] = 0

	return
if __name__ == "__main__":	
	boderx = 5
	bodery = 4
	p=3
	q=2
	minstep = 9999	
	book = [0] * boderx	
	for i in range(0,boderx):
		book[i] = [0]*bodery
	mapblock = [[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
	move = [[0,1],[1,0],[0,-1],[-1,0]]
	dfs(0,0,0)
# -*- coding: utf8 -*-
# author = ZhnJa
# Updated at 20170623
#

def output(n):
	pos=(0,0)
	result=[]
	for i in range(n):
		result.append([])
	for i in xrange(n):
		for j in xrange(n):
			result[i].append(0)
	

	for i in range(1,n*n):
		result[pos(0),pos(1)]=i

def change():
	

		return direction

if __name__ == "__main__":
	d=[[0,1],[1,0],[0,-1],[-1,0]]
	direction = d[0]
	output(4)
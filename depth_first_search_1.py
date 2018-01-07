# -*- coding: utf8 -*-
# author = ZhnJa
# Depth First Search,Page79

def dfs(step):
	#判断数字都放完
	if step == 9:
		step = 0
		global n
		n = n+1
		if alist[0]*100+alist[1]*10+alist[2]+alist[3]*100+alist[4]*10+alist[5] \
			== alist[6]*100+alist[7]*10+alist[8]:
			n = n + 1
			print alist
			return
		else:
			return
		#继续放数字
	for i in range(0,9):
		if book[i] == 0:
			alist[step] = i+1
			book[i] = 1
			dfs(step+1)
			book[i] = 0
	return step


if __name__ == "__main__":
	n = 0
	step = 0
	alist = [0]*9
	book = [0]*9
	dfs(0)
	print n/2

# -*- coding: utf8 -*-
# author = ZhnJa
# 2017-03-24 农药召唤师
# A影忍之足 690     D泣血之刃 1740
# B巨人之握 1500    E无尽战刃 2140
# C破甲弓 2100    F贤者的庇护 2080


items = { 'A':690,'B':1500,'C':2100,'D':1740,'E':2140,'F':2080}
total = 10000
packs = []
result = []
	
def buy_next(money):
	if len(packs) == 6:
		print packs

def dfs():
	buy_next(total)
	print result

if __name__ == '__main__':
	dfs()

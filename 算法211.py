#page26
# -*- coding: utf8 -*-
qq = [6,3,1,7,5,8,9,2,4]

def unlock(alist):
 	blist = []
 	while alist != None :
 		blist.append(alist.pop(0))
 		if len(alist):
 			alist.append(alist.pop(0))
 		else:
 			return blist
	return blist

if __name__ == "__main__":	
	print unlock(qq)
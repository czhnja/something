#-*- coding: utf-8 -*-
#单元排序

temp = [2,4,5,8,9,3,11,88,55,33]
#temp = [1,8,3,6,4]


i = -1
while((i+1) != len(temp)):
	i = i + 1
	j = i + 1
	minIndex = i
	minVal = temp[i]
	for k in range(j,len(temp)):
		if temp[k] < minVal:
			minVal = temp[k]
			minIndex = k
	if minVal != temp[i]:
		tempVal = temp[i]
		temp[i] = minVal
		temp[minIndex] = tempVal
print temp




# -*- coding: utf8 -*-
# author = ZhnJa
# 最常用的快速排序法
import random
import datetime


def quicksort(nums):
	n=len(nums)	
	basicsort(nums,0,n-1)
	return nums

def basicsort(nums,left,right):
	#递归结束条件
	if left > right:
		return 
	temp = nums[left] #基准数
	i = left#左边的序号
	j = right#右边的序号
	while i != j:
		#右往左找
		while (nums[j] >= temp and i < j ):
			j=j-1
		#左往右找
		while (nums[i] <= temp and i < j ):
			i=i+1
		#交换数字
		if i < j:
			(nums[i],nums[j]) = (nums[j],nums[i])
		if i >= j:
			break
	#交换基准数
	nums[left] = nums[i]
	nums[i] = temp
	#递归
	basicsort(nums,left,i-1)
	basicsort(nums,i+1,right)
	return nums

if __name__ == "__main__":	
	alist = [6,1,2,7,9,3,4,5,10,8,8]
	#生成一个大的随机数列
	blist = []
	for i in range(0,10000):
		blist.append(random.randint(0,65535))
	endtime = datetime.datetime.now()

	#测试用时
	starttime = datetime.datetime.now()
	result = quicksort(blist)
	endtime = datetime.datetime.now()
	print 'Quicksort is using:',(endtime - starttime)

	#python内置排序
	starttime = datetime.datetime.now()
	result = blist.sort()
	endtime = datetime.datetime.now()
	print 'Sort is using:',(endtime - starttime)
#sum_fact.py
# -*- coding: utf-8 -*- 
#1부터 n까지의 합을 구하는 재귀 알고리즘 

def sum_fact(n):

	if n==0:
		return 0
	return sum_fact(n-1) + n

print(sum_fact(10))
print(sum_fact(100))
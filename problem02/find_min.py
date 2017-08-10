#find_min2.py
# -*- coding: utf-8 -*- 
#숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def find_min(a):
	n = len(a)
	min_value = a[0]

	for i in range(1,n):
		if a[i] < min_value:
			min_value = a[i]

	return min_value

def input_num():
	num = input('Enter number(s): ').split(',')
	number = list(map(int, num))
	return number

x = input_num()
print("list:", x)
print(find_min(x))
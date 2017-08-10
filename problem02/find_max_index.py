#find_max2.py

def find_max(a):
	n = len(a)
	max_index = 0

	for i in range(1,n):
		if a[i]>a[max_index]:
			max_index = i

	return max_index

list=[17,92,18,33,58,7,33,42]
print(find_max(list))
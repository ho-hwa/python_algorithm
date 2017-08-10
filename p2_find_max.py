#find_max.py

def find_max(a):
	n = len(a)
	max_value = a[0]

	for i in range(1,n):
		if a[i] >= max_value:
			max_value = a[i] 

	return max_value

list = [17,92,18,33,58,7,33,43]
print(find_max(list))

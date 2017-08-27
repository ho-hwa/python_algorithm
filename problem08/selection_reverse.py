#selection.py
#selection sort

def selection_sort(a):
	n = len(a)
	for i in range(0,n-1):
		max_index = i
		for j in range(i+1, n):
			if a[j] > a[max_index]:
				max_index = j
		a[i],a[max_index] = a[max_index],a[i]

d = [2,4,1,5,3]
selection_sort(d)
print(d)

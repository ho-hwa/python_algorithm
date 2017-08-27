#selection.py
#selection sort

def selection_sort(a):
	n = len(a)
	for i in range(0,n-1):
		min_index = i
		for j in range(i + 1, n):
			if a[j] < a[min_index]:
				min_index = j
		a[i],a[min_index] = a[min_index],a[i]

d = [2,4,1,5,3]
selection_sort(d)
print(d)

#binary_rec.py

def binary_sub(a,x,first,last):
	if first>last:
		return -1

	mid = (first + last)//2
	if x == a[mid]:
		return mid
	elif x < a[mid]:
		return binary_sub(a,x,first,mid-1)
	else:
		return binary_sub(a,x,mid+1,last)
	return -1

def binary_search(a,x):
	return binary_sub(a,x,0,len(a)-1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d,16))
print(binary_search(d,81))
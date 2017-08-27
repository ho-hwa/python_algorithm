#binary.py

def binary(a,x):
	first = 0
	last = len(a)-1

	while first <= last:
		mid = (first + last)//2
		if x == a[mid]:
			return mid
		elif x < a[mid]:
			last = mid - 1
		else:
			first = mid + 1

	return -1 #cannot find, print -1

b = [1,4,9,16,25,36,49,64,81]
print(binary(b,16))
print(binary(b,64))
print(binary(b,42))

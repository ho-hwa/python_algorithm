#find_max_rec.py

def find_max(a, n):
	if n == 1:
		return a[0]

	max_value = find_max(a, n - 1)
	if max_value> a[n-1]:
		return max_value
	else:
		return a[n-1]

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))
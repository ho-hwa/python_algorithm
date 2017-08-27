#search.py

def search_list(a,x):
	n = len(a)
	for i in range(0,n):
		if x == a[i]:
			return i

	return -1

q = [17, 92, 18, 33, 58, 7, 32, 42]

print(search_list(q,18))
print(search_list(q,33))
print(search_list(q,900))

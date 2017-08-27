#search2.py

def search_list(a,x):
	n = len(a)
	result = []

	for i in range(0,n):
		if x == a[i]:
			result.append(i)
		
	return result

q = [17, 33, 92, 18, 33, 58, 7, 18, 32, 42]

print(search_list(q,18))
print(search_list(q,33))
print(search_list(q,900))

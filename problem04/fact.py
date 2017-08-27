#fact.py

def fact(n):
	a = 1
	for i in range(1,n+1):
		a = a*i
	return a

print(fact(1))
print(fact(3))
print(fact(5))
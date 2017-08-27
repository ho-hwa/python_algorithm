#gcd2.py

def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

print(gcd(1,5))
print(gcd(3,6))

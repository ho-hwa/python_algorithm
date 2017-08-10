#sum3.py

def sum(num):

	s = 0

	for i in range(1,num+1):
		s = s + i * i
	return s

print(sum(10))
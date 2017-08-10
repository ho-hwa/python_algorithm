#make_a_pair.py

def make_a_pair(a):
	n = len(a)
	group = set()
	for i in range(0,n-1):
		for j in range(i+1,n):
			if a[i] != a[j]:
				group.add(a[i])
				group.add(a[j])
			if len(group) == 2:
				print(group)
				group.clear()

def input_name():
	name = input('Enter name(s): ').split(',')
	name = list(map(str, name))
	return name

x = input_name()
print(make_a_pair(x))
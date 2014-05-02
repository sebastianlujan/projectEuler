#Multiples of 3 or 5 below 1000

def sum(z):
	s = 0
	for i in range(z):
		if ( i % 3 == 0) or ( i % 5 == 0): 
			s = s + i
	return s

print(sum(1000))
#233168

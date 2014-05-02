#Multiples of 3 or 5 below 1000

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum(z):
	s = 0
	for i in range(3,z):
		if ( i % 3 == 0) or ( i % 5 == 0): 
			s = s + i
	return s

print(sum(1000))
#233168 = 10^3

#Elegant Mathematical way using n*(n+1)/2
def sgauss(n,m):
	p = n//m
	return m*p*(p+1)//2

n = 999
print( sgauss(n,3) + sgauss(n,5) - sgauss(n, 15)  )

#Multiples of 3 or 5 below 1000

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Solution 1
def sum(z):
	s = 0
	for i in range(3,z):
		if i % 3 == 0 or i % 5 == 0: 
			s += i
	return s

print(sum(1000))
#233168 = 10^3


#The same algorithm in functional programming
def f(x):
	return sum([y for y in range(3,x) if y % 3 == 0 or y % 5 == 0] )
print(f(1000))


# One line Console solutions
# >>> 
sum( x for x in range(3,1000) if y % 3 == 0 or y % 5 == 0) 
# >>>
sum( x for x in range(3,1000) if not y % 3 or not y % 5) 


#Solution 2
#Elegant Mathematical way using n*(n+1)/2
def sgauss(n,m):
	p = n//m
	return m*p*(p+1)//2

n = 999
print( sgauss(n,3) + sgauss(n,5) - sgauss(n, 15)  )

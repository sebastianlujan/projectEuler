#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
	if n < 2:
		return n 
	fibo, fibo_n, s = 0, 1, 0
	while fibo < n:
		ftemp = fibo + fibo_n
		if not fibo % 2:
			s+=fibo
		fibo = fibo_n
		fibo_n = ftemp
	return s

print(fib(4000000))
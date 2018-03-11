fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
def calc(k): return sum([(fib(i+1)*k[i]) for i in range(0,len(k))])

print(calc(n) == calc(input(m)))




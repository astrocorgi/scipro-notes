import sys

def fib(n):
    a,b = 0, 1
    while b< n:
        print b
        a, b = b, a+b
    print " "

if len(sys.argv) > 2:
    func = sys.argv[1]
    x = int(sys.argv[2])
if func == 'fib':
    fib(x)
elif func == 'fib2':
    fib2(x)
else:
    print "incorrect input"

def fatorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def ma(n):
    result = fatorial(n)
    print(f"{n} ! = {result}")
ma(7)

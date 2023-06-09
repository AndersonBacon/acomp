from time import process_time_ns as ns

def sa(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            s += 1
    return s

def sb(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s

def sc(n):
    return n * (n + 1) / 2

n1 = ns()
r=sa(10000)
n2 = ns()
print(n2-n1)

n1 = ns()
r=sb(10000)
n2 = ns()
print(n2-n1)

n1 = ns()
r=sc(10000)
n2 = ns()
print(n2-n1)
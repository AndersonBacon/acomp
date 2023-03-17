n = int(input())
degree = 0

def soma_n(n):
  return sum(int(d) for d in str(n))
  
while n > 9:
  n = soma_n(n)
  degree = degree + 1

print(degree)
print(n)

if n != 9:
  print(False)
else:
    print(True)
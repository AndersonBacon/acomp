def fatorial(n):
    # Caso base: O fatorial de 0 é 1.
    if n == 0:
      return 1

    # O fatorial de um número n é: n * fatorial(n - 1).
    return n * fatorial(n - 1)

n= fatorial(5)

print(n)
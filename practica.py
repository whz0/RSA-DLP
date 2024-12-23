import random 

def Miller_Robin(n,k):
    # n: numero a verificar
    # k: numero de iteraciones
    # return: True si es primo, False si no lo es
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def main():
    n = 100
    k = 10
    print("Prueba de primalidad de Miller-Robin")
    print(f"n = {n}, k = {k}")
    if Miller_Robin(n, k):
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")
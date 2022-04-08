from random import randint

def dez_mr(num):
    if num%2==0:
        return False

    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for testes in range(10):
        b = randint(1, num - 1)
        resto = pow(b, s, num)

        if resto != 1:
            i = 0
            while resto != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    resto = (resto ** 2) % num
    return True

def gera_primos(x):
    n = randint(pow(10,x),pow(10,x+2))
    while dez_mr(n) != True:
        n = randint(pow(10, x), pow(10, x + 2))
    print(f"{n} é primo")
    return n

def gera_chaves(x):
    p = randint(pow(10,x),pow(10,))


numero = int(input("Escreva um numero:"))
gera_primos(numero)



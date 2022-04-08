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

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def inverso(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m



def gera_chaves():
    p = randint(pow(10,49),pow(10,50))
    while dez_mr(p) != True:
        p = randint(pow(10,49), pow(10,50))
    q = randint(pow(10,99), pow(10,100))
    while dez_mr(q) != True:
        q = randint(pow(10,99), pow(10,100))

    phi = (p - 1) * (q - 1)
    e=0
    for i in range(2,phi+1):
        if mdc(phi,i) == 1:
            e=i
            break

    print (f"Chave p: {p}. Com {len(str(p))} digitos")
    print (f"Chave q: {q}. Com {len(str(q))} digitos")
    n = (p * q)
    print (f"Chave n: {n}. Com {len(str(n))} digitos")
    print(f"phi: {phi}")
    print(f"Chave e: {e}")
    d = inverso(e,phi)
    print(f"Chave d: {d}")
    inpmodq = inverso(p,q)
    print(f"O inverso de p módulo q: {inpmodq}")
    inqmop = inverso(q,p)
    print(f"O inverso de q módulo p: {inqmop}")
    reduzp = d%(p-1)
    print(f"A forma reduzida de d módulo p-1: {reduzp}")
    reduzq = d%(q-1)
    print(f"A forma reduzida de d módulo q-1: {reduzq}")



gera_chaves()



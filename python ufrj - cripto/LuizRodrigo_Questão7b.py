numcar = [561, 1105, 1729, 2465, 2821, 6601, 8911]

def comprim(n):
    if 1 < n <=10000:
        if n in numcar:
            print(f"{n} é um número composto")
        for i in range(2,n):
            if pow(i,n)%n != i:
                print(f"{n} é um numero composto")
                break
        else:
            print(f"{n} é um numero primo")
    else:
        print("Digite um número entre 1 a 10000")

num = int(input("Digite um numero: "))
comprim(num)
n = int(input("Digite um número inteiro positivo:"))

listaltcomp = []

def div(x):
    divisores = []
    for i in range(1,x+1):
        if x%i == 0:
            divisores.append(i)
    return int(len(divisores))

def altcomp(x):
    for k in range(x, 0, -1):
        if (k-1 < k) & (div(k-1) < div(k)):
            listaltcomp.append(k)

altcomp(n)
print(f'O número {n} possui {len(listaltcomp)} números altamentos compostos menores ou iguais a ele, sendo eles {listaltcomp}')
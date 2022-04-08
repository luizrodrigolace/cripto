listaprimos = [2, 3, 5, 7, 11, 13, 17, 19, 23,
               29, 31, 37, 41, 43, 47, 53, 59,
               61, 67, 71, 73, 79, 83, 89, 97,
               101, 103, 107, 109, 113, 127,
               131, 137, 139, 149, 151, 157,
               163, 167, 173, 179, 181, 191,
               193, 197, 199, 211, 223, 227,
               229, 233, 239, 241, 251, 257,
               263, 269, 271, 277, 281, 283,
               293, 307, 311, 313, 317]


def funcpseudo(limite, base):
    listapseudo = []
    if limite <= pow(10, 5) and base >= 2:
        for i in range(2, limite + 1):
            if (base ** (i - 1)) % i == 1:
                for primo in listaprimos:
                    if i % primo == 0:
                        if i/primo != 1:
                            listapseudo.append(i)
                            break

    print(listapseudo)
    print(len(listapseudo))

a = int(input("Digite uma base: "))
n = int(input("Digite um limite: "))
funcpseudo(n, a)


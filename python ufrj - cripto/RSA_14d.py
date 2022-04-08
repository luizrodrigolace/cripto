tabelinha = {'0': 111, '1': 112, '2': 113, '3': 114,
             '4': 115, '5': 116, '6': 117, '7': 118,
             '8': 119, '9': 121, '=': 122, '+': 123,
             '−': 124, '/': 125, '∗': 126, 'a': 127,
             'b': 128, 'c': 129, 'd': 131, 'e': 132,
             'f': 133, 'g': 134, 'h': 135, 'i': 136,
             'j': 137, 'k': 138, 'l': 139, 'm': 141,
             'n': 142, 'o': 143, 'p': 144, 'q': 145,
             'r': 146, 's': 147, 't': 148, 'u': 149,
             'v': 151, 'w': 152, 'x': 153, 'y': 154,
             "z": 155, "á": 156, "à": 157, 'â': 158,
             "ã": 159, 'é': 161, 'ê': 162, 'í': 163,
             'ó': 164, 'ô': 165, "õ": 166, "ú": 167,
             'ç': 168, 'A': 169, 'B': 171, 'C': 171,
             'D': 173, 'E': 174, 'F': 175, 'G': 176,
             'H': 177, 'I': 178, 'J': 179, 'K': 181,
             'L': 182, 'M': 183, 'N': 184, 'O': 185,
             'P': 186, 'Q': 187, 'R': 188, 'S': 189,
             'T': 191, 'U': 192, 'V': 193, 'W': 194,
             'X': 195, 'Y': 196, 'Z': 197, 'Á': 198,
             'À': 199, 'Â': 211, 'Ã': 212, 'É': 213,
             'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217,
             'Õ': 218, 'Ú': 219, 'Ç': 221, ',': 222,
             '.': 223, '!': 224, '?': 225, ';': 226,
             ':': 227, '_': 228, '(': 229, ')': 231,
             '"': 232, '#': 233, '$': 234, '%': 235,
             '@': 236, ' ': 237, ''
                                 '': 238}

inv_tabelinha = {v: k for k, v in tabelinha.items()}


def encriptar(texto, n, e):
    # print(texto)
    lista = []
    lista = list(texto)
    textonum = []
    for i in range(0, len(lista)):
        textonum.append(tabelinha[lista[i]])
    # print(textonum)
    letrasemnum = str()

    for i in range(0, len(textonum)):
        letrasemnum += str(textonum[i])

    # print(int(letrasemnum))
    blocos = []
    for i in range(0, len(letrasemnum)):
        blocos.append(letrasemnum[10 * i:10 * (i + 1)])
        if '' in blocos:
            blocos.remove('')

    # print(blocos)
    blocoscriptostrg = []

    # print(blocos[0])
    for i in range(0, len(blocos)):
        blocoscriptostrg.append(str(pow(int(blocos[i]), e, n)))

    blococriptoint = []
    for val in blocoscriptostrg:
        blococriptoint.append(int(val))

    print(f"Mensagem criptografada em blocos: {blococriptoint}")
    return (blococriptoint)


def descriptar(x, n, d):
    blocos2 = x
    blocosdescriptados = []
    for i in range(0, len(blocos2)):
        blocosdescriptados.append(pow(blocos2[i], d, n))

    print(f"Mensagem descriptografada em blocos {blocosdescriptados}")

    blocosdescrip_str_sep = []
    for i in range(0, len(blocosdescriptados)):
        blocosdescrip_str_sep.append(str(blocosdescriptados[i]))

    print(blocosdescrip_str_sep)

    str_junt = ''
    for i in range(0, len(blocosdescrip_str_sep)):
        str_junt += blocosdescrip_str_sep[i]
    print(str_junt)

    bloco_int_junt = []
    bloco_int_junt.append(str(str_junt))
    # print(bloco_int_junt)

    bloco_int_sep = []
    for i in range(0, len(str_junt)):
        bloco_int_sep.append(str_junt[0 + 3 * i:3 + 3 * i])
        if '' in bloco_int_sep:
            bloco_int_sep.remove('')
    print(bloco_int_sep)

    mensagem_letras_num = []
    for val in bloco_int_sep:
        mensagem_letras_num.append(int(val))

    texto_descrip = ""
    for i in range(0, len(mensagem_letras_num)):
        texto_descrip += inv_tabelinha[mensagem_letras_num[i]]

    print(texto_descrip)


texto = list(input("Escreva algo: "))
n = int(input("Digite a chave publica n: "))
e = int(input("Digite a chave publica e: "))
d = int(input("Digite a chave secreta d: "))

# encriptar(texto,n,e)
descriptar(encriptar(texto, n, e), n, d)

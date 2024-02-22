def cont(frase):
    palavras = frase.split()
    contador = {}
    
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return contador

frase = input ("FRASE:")
resultado = cont(frase)
print(resultado)

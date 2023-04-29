def criptografia(linhaTexto, colunaTexto):
    for linha in alfabeto:
        if colunaTexto in linha:
            posiçãoColuna = linha.index(colunaTexto)
        if linhaTexto in linha:
            posiçãoTexto = linha.index(linhaTexto)
    
    #Caso estejam na mesma coluna
    if posiçãoColuna == posiçãoTexto:
        for indice, linha in enumerate(alfabeto):
            if linhaTexto in linha:
                if indice == 4:
                    elemento = alfabeto[0][posiçãoTexto]
                else:
                    elemento = alfabeto[indice+1][posiçãoTexto]
                return elemento
            
    for linha in alfabeto:
        #Caso estejam na mesma linha
        if colunaTexto in linha and linhaTexto in linha:
            if posiçãoTexto == 4:
                posiçãoTexto = 0
            else:
                posiçãoTexto += 1
            elemento = linha[posiçãoTexto]
            return elemento
        
        #Caso estejam em linhas e colunas diferentes(Padrão)
        elif linhaTexto in linha:
            elemento = linha[posiçãoColuna]
            return elemento

def descriptografia(linhaTexto, colunaTexto):
    for linha in alfabeto:
        if linhaTexto in linha:
            posiçãoTexto = linha.index(linhaTexto)
        if colunaTexto in linha:
            posiçãoColuna = linha.index(colunaTexto)

    #Caso estejam na mesma coluna
    if posiçãoColuna == posiçãoTexto:
        for indice, linha in enumerate(alfabeto):
            if linhaTexto in linha:
                if indice == 0:
                    elemento = alfabeto[4][posiçãoTexto]
                else:
                    elemento = alfabeto[indice-1][posiçãoTexto]
                return elemento
            
    for linha in alfabeto:
        #Caso os itens estejam na mesma linha
        if colunaTexto in linha and linhaTexto in linha:
            posiçãoTexto -= 1
            elemento = linha[posiçãoTexto]
            return elemento

        #Caso estejam em linhas e colunas diferentes(Padrão)
        elif linhaTexto in linha:
            elemento = linha[posiçãoColuna]
            return elemento
        

palavraChave = input('\nInsira a palavra-chave: ').lower()

while True:
    while True:
        opc = input('''\nO que deseja:
    [1] Criptografar mensagem
    [2] Descriptografar mensagem
    [3] Mudar a palavra-chave
    [0] Sair
    Opção: ''')
        if opc in '0123':
            break
        else:
            print("Insira alguma das opções!")

    alfabeto = ['a','b','c','d','e','f','g','h','i/j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listaPalavraChave = list(palavraChave[::-1])
    tamanhoLista = len(listaPalavraChave)
    pos = 0

    #--Tratamento da palavra-chave--

    #Removendo as letras iguais na palavra-chave
    while True:
        if pos == tamanhoLista:
            pos = 0
            break
        for x in range(tamanhoLista):
            if pos != x:
                if listaPalavraChave[x] == 'i' or listaPalavraChave[x] == 'j':
                    listaPalavraChave[x] = 'i/j'
                if listaPalavraChave[pos] == listaPalavraChave[x]:
                    listaPalavraChave.remove(listaPalavraChave[pos])
                    pos = 0
                    break
        tamanhoLista = len(listaPalavraChave)
        pos += 1

    #--Tratamento do alfabeto --

    #Removendo as letras iguais do alfabeto que estejam na palavra-chave
    for letraP in listaPalavraChave:
        for letraA in alfabeto:
            if letraP == letraA:
                alfabeto.remove(letraA)

    #Inserindo a palavra-chave no alfabeto
    for letra in listaPalavraChave:
        alfabeto.insert(0,letra)

    #Dividindo o alfabeto em 5 sublistas
    listaAux = []
    listaCompleta = []
    for x in range(25):
        pos += 1
        listaAux.append(alfabeto[x])
        if pos % 5 == 0:
            listaCompleta.append(listaAux)
            listaAux = []

    pos = 0

    alfabeto = listaCompleta.copy()

    #Criptografia
    if opc == '1':
        textoClaro = input('Insira o texto que deseja criptografar: ').lower()

        #--Tratamento do texto--
        textoClaro = list(textoClaro)

        #Tirando espaços em branco
        while True:
            if pos == len(textoClaro):
                pos = 0
                break
            if textoClaro[pos] == ' ':
                textoClaro.pop(pos)
            pos+=1

        #Adicionando um x caso tenha letras repetidas
        for x in range(len(textoClaro)):
            for y in range(x+1,len(textoClaro)):
                if textoClaro[x] == textoClaro[y]:
                    textoClaro[x] = textoClaro[x] + 'x'
                    break
                else:
                    break

        textoClaro = ''.join(textoClaro)


        #Adicionando um x caso fique alguma letra sozinha no final
        if len(textoClaro) % 2 != 0:
            textoClaro = textoClaro + 'x'

        #Dividindo o texto de 2 em 2
        listaAux = []
        listaCompleta = []
        for x in range(len(textoClaro)):
            pos+=1
            listaAux.append(textoClaro[x])

            for i, letra in enumerate(listaAux):
                if 'i' == letra or 'j' == letra:
                    listaAux[i] = 'i/j'

            if pos % 2 == 0:
                listaCompleta.append(listaAux)
                listaAux = []

        textoClaroDividido = listaCompleta.copy()
        listaAux = []
        listaCompleta = []

        #--Criptografia PlayFair--
        for lista in textoClaroDividido:

            primeiroAux = lista[0]
            segundoAux = lista[1]

            primeiro = criptografia(primeiroAux,segundoAux)
            segundo = criptografia(segundoAux,primeiroAux)

            listaAux.append(primeiro)
            listaAux.append(segundo)
            listaCompleta.append(listaAux)
            listaAux = [] 

        #Juntando os elementos criptografados
        for sublista in listaCompleta:
            for elemento in sublista:
                listaAux.append(elemento)

        listaAux = ''.join(listaAux)

        mensagemCriptografada = listaAux
    
        print(f"\nA sua mensagem criptografada: {mensagemCriptografada}")

    #Descriptografia
    elif opc == '2':
        textoCriptografado = input("Insira o texto que deseja descriptografar: ")

        #--Tratamento do texto--
        textoCriptografado = list(textoCriptografado)

        #Dividindo o texto de 2 em 2
        listaAux = []
        listaCompleta = []

        for x in range(len(textoCriptografado)):
            pos+=1
            listaAux.append(textoCriptografado[x])

            for i, letra in enumerate(listaAux):
                if '/' == letra or 'j' == letra:
                    listaAux.remove(letra)

            for i, letra in enumerate(listaAux):
                if 'i' == letra or 'j' == letra:
                    listaAux[i] = 'i/j'

            if pos % 2 == 0:
                listaCompleta.append(listaAux)
                listaAux = []

        for elemento in listaCompleta:
            if elemento == []:
                listaCompleta.remove(elemento)

        #--Descriptografia playfair--
        listaAuxDesc = []
        listaCompletaDesc = []

        for lista in listaCompleta:

            primeiroAuxDesc = lista[0]
            segundoAuxDesc = lista[1]

            primeiroDesc = descriptografia(primeiroAuxDesc, segundoAuxDesc)
            segundoDesc = descriptografia(segundoAuxDesc, primeiroAuxDesc)

            listaAuxDesc.append(primeiroDesc)
            listaAuxDesc.append(segundoDesc)
            listaCompletaDesc.append(listaAuxDesc)
            listaAuxDesc = []

        #Juntando os elementos descriptografados
        for sublista in listaCompletaDesc:
            for elemento in sublista:
                listaAuxDesc.append(elemento)

        listaAuxDesc = ' '.join(listaAuxDesc)
        mensagemDescriptografada = listaAuxDesc


        print(f"\nA sua mensagem descriptografada: {mensagemDescriptografada}")

    elif opc == '3':
        palavraChave = input('\nInsira a palavra-chave: ').lower()
    
    elif opc == '0':
        print("Saindo do programa...")
        break

#Grupo = Paulo Miguel Benevenuto, Carlos Eduardo e Renato

#FUNÇÃO VALIDAR LETRAS (VERIFICANDO MINÚSCULA E APENAS LETRAS)
def validar_letras(palavra):
    #LISTA COM CARACTERES
    carac = ['.',',','?','!','-']
    #FOR PERCORRENDO LISTA DE CARACTERES
    for item in carac:
        #FOR PERCORRENDO A PALAVRA
        for letra in palavra:
            #CONDIÇÃO SE CARACTER FOR IGUAL A LETRA
            if item in letra:
                #TROCA O CARACTER POR ESPAÇO VAZIO
                palavra = palavra.replace(item,'')
    #VERIFICANDO SE É MINÚSCULO E SE TEM APENAS LETRAS            
    if not palavra.islower() or not palavra.isalpha():
        return False
    
    return True

#FUNÇÃO VALIDAR HIFEN
def validar_hifen(palavra):
    #CONTADOR PARA VERIFICAR QUANTOS HIFENS POSSUI A PALAVRA
    qtd_hifen = palavra.count('-')
    #CONDIÇÃO: COMEÇAR COM HIFEN MAIS DE UM HIFEN, E TERMINAR COM HIFEN = FALSE
    if qtd_hifen > 1  or palavra.startswith('-') or palavra.endswith('-'):
        return False
    else:
        return True

#FUNÇAO VALIDAR PONTUAÇÃO
def validar_pontuacao(palavra):
    #LISTA COM PONTUAÇÕES
    pontuacao = ['.',',','?','!']
    #FOR PERCORRENDO A LISTA DE PONTUAÇÕES
    for item in pontuacao:
        #FOR PERCORRENDO A PALAVRA, MENOS A ÚLTIMA LETRA (SLICING)
        for letra in palavra[:-1]:
            #CONDIÇÃO: SE PONTUAÇÃO ESTIVER NA LETRA = FALSE
            if item in letra:
                return False

    return True

#FUNÇÃO PARA LER O ARQUIVO
def ler_arquivo():
    #ABRE ARQUIVO
    arquivo = open('frases.txt','r')
    #LER ARQUIVO
    conteudo = arquivo.read()
    #FECHA ARQUIVO
    arquivo.close()
    return conteudo

#FUNÇÃO PARA CHAMAR TODAS AS FUNÇÕES
def principal():
    #VARIÁVEL PARA RECEBER O CONTEUDO DO .TXT
    conteudo = ler_arquivo()

    #TROCANDO A QUEBRA DE LINHA POR ESPAÇO VAZIO
    frase = conteudo.replace('\n',' ')

    #TRANSFORMANDO TUDO EM UMA LISTA COM CADA PALAVRA SEPARADA POR ESPAÇO
    palavra_separada = frase.split(' ')

    #VARIÁVEL PARA RECEBER QUANTIDADE DE PALAVRAS VÁLIDAS
    qtd = 0
    
    #FOR PERCORRENDO OS ITENS DA LISTA palavra_separada
    for palavra in palavra_separada:
        #VALIDAÇÃO: SE TODAS AS FUNÇÕES RETORNAREM 'TRUE'. SOMA NO CONTADOR DAS PALAVRAS VÁLIDAS      
        if validar_letras(palavra) == True and validar_pontuacao(palavra) == True and validar_hifen(palavra) == True:
            qtd+=1
            
    #RETORNA A QUANTIDADE DE PALAVRAS VÁLIDAS        
    return qtd

print('Quantidade de palavras válidas: ',principal())
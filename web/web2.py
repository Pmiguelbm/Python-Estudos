def verifica_cadastro(nome, idade):
  nome = nome.lower()
  alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
  valida = True
  for letra in nome:
    if letra not in alfabeto:
        valida = False
  if valida == True and idade.isdigit():
    return True
  else:
    return False

def cadastro_cliente(nome, idade):
  arquivo = open('cadastro.txt', 'a')
  nome = nome.lower()
  arquivo.write(nome + '.' + idade + '\n')
  arquivo.close()

  return nome, idade

def pesquisa_cliente(nome):
  arquivo = open('cadastro.txt', 'r')
  lista_de_cliente = arquivo.read()
  arquivo.close()
  lista_cadastro = lista_de_cliente.replace('\n', '.')
  lista_cadastro = lista_cadastro.split('.')
  nome = nome.lower()
  if nome in lista_cadastro:
    posicao = lista_cadastro.index(nome)
    return '\nO nome do cliente é [{}] e a idade é [{}].'.format(
      nome.capitalize(), lista_cadastro[posicao + 1])
  else:
    return 'Cadastro inexistente'


flag = 's'
while flag == 's':

  nome = input('Nome: ')
  idade = input('Idade: ')
  if verifica_cadastro(nome, idade) == True:
    cadastro_cliente(nome, idade)
  else:
    print('Dados incorretos! Reecreva de forma correta.')
  flag = input('Deseja continuar? s ou n: ').lower()

flag2 = 's'
print('\nPESQUISA DE CADASTRO:\n')
while flag2 == 's':
    busca = input('Nome: ')
    print(pesquisa_cliente(busca))
    flag2 = input('\nDeseja continuar a pesquisar? s ou n: ').lower()
#Uma empresa quer que você crie um programa que vai receber dados de clientes(Nome e Idade) em formato de  string e depois deve acessa-los. Os dados de nome não podem ter caracteres especiais ou números , como exemplo: '/','#','@','!','&'.
#Dados de idade não podem ter letras ou caracteres especiais.
#O nome cadastrado pode ser pesquisado após o cadastro, e deve trazer os dados 'Nome e Idade'.

def entrada_nomes(entrada_nome):
  carac = ['/','#','@','!','&','$','"','*','-','%','¨','(',')']
  numeros = ['0','1','2','3','4','5','6','7','8','9']
  verifica = False
  nome_minusculo = entrada_nome.lower()
  for busca in nome_minusculo:
    for busca_carac in carac: 
      for busca_numeros in numeros:
        if busca in busca_carac or busca in busca_numeros:
          verifica = True
  if verifica == True:
    return '\nExiste um nome com caracteres inválidos!'
  else:
    entrada_idade = input('digite sua idade:')
    return entrada_idades(entrada_idade)

def entrada_idades(entrada_idade):
  letras = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q']
  carac = ['/','#','@','!','&','$','"','*','-','%','¨','(',')']
  verifica = False
  for busca_idade in entrada_idade:
    for busca_carac in carac:
      for busca_letras in letras:
        if busca_idade in busca_carac or busca_idade in busca_letras:
          verifica = True
  if verifica == True:        
    return '\nExiste caracteres inválidos na idade!'
  else:
    print('\nDados Cadastrados com sucesso!')
    pedido = ''
    while pedido != 'não':
      pedido = input('\nVocê deseja ver os dados que foram cadastrados? \n[Responda com sim/não]: ')
      if pedido == 'sim':
        return('\nO nome do cliente é [{}] e a idade é [{}].'.format(entrada_nome, entrada_idade))
        break
      else:
        return '\nSistema encerrado!'
        
entrada_nome = input('Digite seu nome:')

print(entrada_nomes(entrada_nome))


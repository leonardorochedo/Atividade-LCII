#Implemente um programa em Python que receba uma string digitada por um usuário e seja capaz de identificar se essa string representa um número de telefone. Para isso, a string deve estar no seguinte formato: (DD) DDDDD-DDDD

import re # Importando Expressões Regulares

cell = str(input("Digite seu número de celular com todos os 11 digitos no seguinte formato '(DD) DDDDD-DDDD': ")) # Pegando o numero de telefone

pattern = re.compile(r'\s+')
cell = re.sub(pattern, '', cell) # Tirando o espaço do numero

pattern = re.compile(r'\D+') 
cell = re.sub(pattern, '', cell) # Tirando as strings no meio dele

verificacao = bool((re.search(r'\d', cell))) # Verificando se tem algum dígito no número True = sim / False = não

if verificacao == True: # Se tiver algum número vai fazer isso para verificar se tem o tanto de numeros corretos de um celular padrão
  print("Verificando se você digitou seu número corretamente...")
  lista = list(cell) # Transformando o numero de celular em uma lista
  numlista = len(lista) # Lendo quantos números tem nessa lista
  if numlista == 11:
    print("Legal! Seu número foi avaliado e certamente é um número de celular, Obrigado.")
  else:
    print("Ooops. Seu número não está cumprindo os termos requisitados, por favor tente novamente!")
else:
  print("Você não digitou certo! Tente novamente")
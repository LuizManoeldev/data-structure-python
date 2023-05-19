from ab import Arvore
from avl import AVLTree

with open('dicionario.txt') as f:
    conteudo_abb = f.readlines()
conteudo_abb = [x.rstrip('\n') for x in conteudo_abb] 

with open('dicionario.txt') as f:
    conteudo_avl = f.readlines()
conteudo_avl = [x.rstrip('\n') for x in conteudo_avl] 


# Inserindo todas as palavras do arquivo 'dicionario.txt'
def carregar_abb():
  contador = 0
  arvore_bb = Arvore()
  for i in conteudo_abb:
    contador = contador + arvore_bb.add(i) # A propria operação de busca retorna quantas recursões ate encontrar o valor
  print(f'NUMERO DE OPERAÇÕES PARA ADICIONAR {len(conteudo_abb)} PALAVRAS NA ABB = {contador}')
  return arvore_bb


# Inserindo todas as palavras do arquivo 'dicionario.txt'
def carregar_avl():
  contador = 0
  arvore_avl = AVLTree()
  for i in conteudo_avl:
    contador = contador + arvore_avl.insert(i) # A propria operação de busca retorna quantas recursões ate encontrar o valor
  print(f'NUMERO DE OPERAÇÕES PARA ADICIONAR {len(conteudo_avl)} PALAVRAS NA AVL = {contador}')  
  return arvore_avl



def buscar_abb(arvore, numero_de_palavras):
  contador = 0
  for i in range(numero_de_palavras):
    chave = conteudo_abb[i]
    contador = contador + arvore.busca(chave) # A propria operação de busca retorna quantas recursões ate encontrar o valor
  print(f'NUMERO DE OPERAÇÕES PARA BUSCAR {numero_de_palavras} PALAVRAS NA ABB = {contador}')

def remover_abb(arvore, numero_de_palavras):
  contador = 0
  for i in range(numero_de_palavras):
    chave = conteudo_abb[i]
    contador = contador + arvore.remover(chave) # A propria operação de busca retorna quantas recursões ate encontrar o valor
    del conteudo_abb[i]
  print(f'NUMERO DE OPERAÇÕES PARA REMOVER {numero_de_palavras} PALAVRAS DA ABB = {contador}') 


def buscar_avl(arvore, numero_de_palavras):
  contador = 0
  for i in range(numero_de_palavras):
    chave = conteudo_abb[i]
    contador = contador + arvore.find(chave) # A propria operação de busca retorna quantas recursões ate encontrar o valor
  print(f'NUMERO DE OPERAÇÕES PARA BUSCAR {numero_de_palavras} PALAVRAS NA AVL = {contador}') 
  

def remover_avl(arvore, numero_de_palavras):
  contador = 0
  for i in range(numero_de_palavras):
    chave = conteudo_avl[i]
    contador = contador + arvore.remove(chave) # A propria operação de busca retorna quantas recursões ate encontrar o valor
    conteudo_avl.pop(i)
  print(f'NUMERO DE OPERAÇÕES PARA REMOVER {numero_de_palavras} PALAVRAS DA AVL = {contador}')



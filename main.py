from functions import carregar_abb, carregar_avl, buscar_abb, buscar_avl, remover_abb, remover_avl

if __name__ == "__main__":

  #Chamando funçao que inicia a arvore, inserindo todas as palavras do arquivo 'dicionario.txt'
  arvore_bb = carregar_abb()
  arvore_avl =  carregar_avl()
  print()

  
  # Operações passadas na atividade do professor
  # É chamada uma função auxiliar que recebe a arvore a ser usado e numero de opeções a serem executadas.
  buscar_abb(arvore_bb, 1000)
  remover_abb(arvore_bb, 2000)
  buscar_abb(arvore_bb, 1000)
  
  print()
  
  buscar_avl(arvore_avl, 1000)
  remover_avl(arvore_avl, 2000)
  buscar_avl(arvore_avl, 1000)

  
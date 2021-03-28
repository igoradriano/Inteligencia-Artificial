import numpy as np
import random

class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade  #parâmetro da classe construtora é passado como valor do atributo da classe
    self.ultima_posicao = -1    #vetor vazio logo no inicio recebe ultima aposição = -1
    self.valores = np.empty(self.capacidade, dtype=int) #A função empty () é usada para criar um novo array numpy vazio com a capacidade que passaremos, e tipo de dados inteiro.
    
  # O(n) --> MÉTODO PARA IMPRIMIR OS DADOS ---------------------------------------------------------------------

  def imprime(self):
    if self.ultima_posicao == -1:  
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):  #para o primeiro caso será será -1(array vazio) + 1(primeiro termo) = 0 (tamanho do array)
        print(i, ' - ', self.valores[i])  #dessa forma, só iremos imprimir os próximos termos do array através do range(ultima_posicao)

  # O(n)  --> MÉTODO PARA INSERIR DADOS ------------------------------------------------------------------------

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1: 
      print('Capacidade máxima atingida')
      return

  # --------> PESQUISA POR VALOR NO ARRAY E RETORNA A POSIÇÃO QUE DEVE SER INSERIDO O NOVO VALOR ---------------

    posicao = 0
    for i in range(self.ultima_posicao + 1):   #para o primeiro caso será será -1(array vazio) + 1(primeiro termo) = 0 (tamanho do array)
      posicao = i
      if self.valores[i] > valor:   #se o valor anterior desta posição for maior que o novo valor a ser inserido:
        break
      if i == self.ultima_posicao:  #cqso o valor a ser inserido seja maior que todos os valores do array, atualizar a posição com + 1
        posicao = i + 1

  #---------> AFASTA VALORES CASO NECESSÁRIO E DEPOIS INSERE O VALOR DESEJADO ----------------------------------
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]  #jogando os valores do vetor para o final do vetor, abrindo espaço para inserir novo valor
      x -= 1

    self.valores[posicao] = valor  #insere o valor na posição que descobrimos com a PESQUISA
    self.ultima_posicao += 1  #Atualiza o valor da ultima posição 
#----------------------------------------------------------------------------------------------------------------
  # O(n) PESQUISA LINEAR
  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:   # se o valor do vetor naquela posicao for maior que o valor que estou procurando
        print("Já passamos por um valor maior que o procurado, significa que ele não está presente no vetor")
        return -1
      if self.valores[i] == valor:   # se o valor do vetor naquela posicao for igual ao valor que estou procurando retorne a posicao deste valor no vetor
        print(f"A posição do seu valor é :{i}")
        return i
      if i == self.ultima_posicao:    # se a posição onde parou a pesquisa for igual a ultima posicao 
        print("Chegamos ao final do vetor e nada foi encontrado")
        return -1
        
#---------------------------------------------------------------------------------------------------------------
  # O(log n) PESQUISA BINÁRIA
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao
    i = 0 #DEBUG
    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)   # Define o centro do vetor
      print(f"Testamos sua posição central {posicao_atual}")
      # Se achou na primeira tentativa
      if self.valores[posicao_atual] == valor:
        print(f"Encontramos o seu valor, foram feitas {i} interacoes ") #DEBUG
        return posicao_atual
      # Se não achou
      elif limite_inferior > limite_superior:
        print(f"Seu valor não está no vetor, foram feitas {i} interacoes") #DEBUG
        return -1
      # Divide os limites
      else:
        i += 1 #DEBUG
        # Limite inferior
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
          print(f"O valor está acima de {self.valores[posicao_atual]}, posicao : {posicao_atual}, mudamos sua posicao inferior para {posicao_atual + 1} / posicao superior pemanece {limite_superior} ") #DEBUG
        # Limite superior
        else:
          limite_superior = posicao_atual - 1
          print(f"O valor está abaixo de {self.valores[posicao_atual]}, posicao: {posicao_atual}, mudamos sua posicao superior para {posicao_atual - 1} / posicao inferior permance {limite_inferior}") #DEBUG

  # O(n)  EXLUSAO ----------------------------------------------------------------------------------------------
  def excluir(self, valor):
    posicao = self.pesquisa_linear(valor) #atualiza a posicao para o indice retornado pela pesquisa linear
    if posicao == -1:  # SE NAO ENCONTRAMOS O VALOR
      return -1
    else:   # CASO ENCONTRE UMA POSICAO NO VETOR, OU SEJA, ENCONTRE O VALOR NO VETOR
      for i in range(posicao, self.ultima_posicao): # PERCORRA DA POSICAO DO VALOR ENCONTRADO ATÉ O FINAL 
        self.valores[i] = self.valores[i + 1] #PEGUE OS VALORES DA POSICAO DA FRENTE E JOGUE PARA POSICAO DE TRAS
      
      self.ultima_posicao -= 1 #ATUALIZA A ULTIMA POSICAO, JÁ QUE EXCLUIMOS UM VALOR DO VETOR

#---------------------------------------------------------------------------------------------------------------
# Testes
#TESTES DE INSERCAO
vetor = VetorOrdenado(10)
vetor.imprime()
print("---------------------")
vetor.insere(6)
vetor.imprime()
print("---------------------")
vetor.insere(4)
vetor.imprime()
print("---------------------")
vetor.insere(3)
vetor.imprime()
print("---------------------")
vetor.insere(5)
vetor.imprime()
print("---------------------")
vetor.insere(1)
vetor.imprime()
print("---------------------")
vetor.insere(8)
vetor.imprime()
print("---------------------")
vetor.imprime()
print("---------------------")

#TESTES DE PESQUISA LINEAR 
vetor.pesquisa_linear(8)
print("---------------------")
vetor.pesquisa_linear(2)
print("---------------------")
vetor.pesquisa_linear(9)
print("---------------------")

# TESTES DE EXCLUSAO
vetor.excluir(5)
vetor.imprime()
print("---------------------")
vetor.excluir(1)
vetor.imprime()
print("---------------------")
vetor.excluir(8)
vetor.imprime()
print("---------------------")
vetor.excluir(9)
print("---------------------")
vetor = VetorOrdenado(10)
vetor.insere(8)
vetor.insere(9)
vetor.insere(4)
vetor.insere(1)
vetor.insere(5)
vetor.insere(7)
vetor.insere(11)
vetor.insere(13)
vetor.insere(2)
vetor.imprime()
print("---------------------")

#TESTES DE PESQUISA BINARIA
vetor.pesquisa_binaria(7)
print("---------------------")
vetor.pesquisa_binaria(5)
print("---------------------")
vetor.pesquisa_binaria(13)
print("---------------------")
vetor.pesquisa_binaria(20)
print("---------------------")

#CRIANDO VETOR 2 ATRAVÉS DE UM LAÇO FOR PARA ADICIONAR ALEATORIAMENTE VALORES DE 0 A 100000 NO VETOR
#OBS: VETOR TEM TAMANHO IGUAL A 200
vetor2 = VetorOrdenado(200)
for i in range(200):
  vetor2.insere(random.randint(0,1000))
print("------------------------------------------------------------------------------------------------------")
vetor2.pesquisa_binaria(145) #PESQUISA BINARIA 
print("------------------------------------------------------------------------------------------------------")
vetor2.pesquisa_linear(145) #PESQUISA LINEAR

#>>> np.empty(2)
#array([  6.95033087e-310,   1.69970835e-316])
#>>> np.empty(32)
#array([  6.95033087e-310,   1.65350412e-316,   6.95032869e-310,
   #      6.95032869e-310,   6.95033051e-310,   6.95033014e-310,
   #      6.95033165e-310,   6.95033167e-310,   6.95033163e-310,
   #      6.95032955e-310,   6.95033162e-310,   6.95033166e-310,
   #      6.95033160e-310,   6.95033163e-310,   6.95033162e-310,
   #      6.95033167e-310,   6.95033167e-310,   6.95033167e-310,
   #      6.95033167e-310,   6.95033158e-310,   6.95033160e-310,
   #      6.95033164e-310,   6.95033162e-310,   6.95033051e-310,
   #     6.95033166e-310,   6.95033161e-310,   2.97403466e+289,
   #      7.55774284e+091,   1.31611495e+294])
#>>> np.empty([2, 2])
#array([[7.74860419e-304, 8.32155212e-317],
   #   [0.00000000e+000, 0.00000000e+000]])
#>>> np.empty([2, 3])
#array([[  6.95033087e-310,   1.68240973e-316,   6.95032825e-310],
   #     [  6.95032825e-310,   6.95032825e-310,   6.95032825e-310]])
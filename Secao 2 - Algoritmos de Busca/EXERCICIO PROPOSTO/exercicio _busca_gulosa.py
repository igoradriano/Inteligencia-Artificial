# Grafo - Busca gulosa
#A Heurística utilizada para esse problema com o método de busca gulosa foi utilizar a menor distancia em linha reta entre o ponto inicial e o ponto final. Não considerados a distancia real.

## Grafo

class Vertice:

  def __init__(self, rotulo, distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = [] #Array que conterá todas as cidades adjacentes a cada cidade objeto tratada

  def adiciona_adjacente(self, adjacente):  # Método da classe Vertice para adicionar cidades adjacentes a lista
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):  # Método da classe Verticce para mostrar as cidades adjacentes de cada Vertice
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo) # i -> representa cada objeto presente dentro da lista adjacentes, vertice.rotulo é para acessar o rótulo de cada objeto presente na lista, uma vez que eles também serao do tipo vertice

class Adjacente:  #Classe onde passaremos um objeto do tipo vertice (outra cidade) e o custo (distancia)
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo

class Grafo: # Esta classe vai unir a Classe Vertice a classe Adjacente
  porto_uniao = Vertice("Porto União", 203)
  paulo_frontin = Vertice("Paulo Frontin", 172)
  canoinhas = Vertice("Canoinhas", 141)
  tres_barras = Vertice("Três Barras", 131)
  sao_mateus_do_sul = Vertice("São Mateus do Sul", 123)
  irati = Vertice("Irati", 139)
  curitiba = Vertice("Curitiba", 0)
  palmeiras = Vertice("Palmeiras", 59)
  mafra = Vertice("Mafra", 94)
  campo_largo = Vertice("Campo Largo", 27)
  balsa_nova = Vertice("Balsa Nova", 41)
  lapa = Vertice("Lapa", 74)
  tijucas_do_sul = Vertice("Tijucas do Sul", 56)
  araucaria = Vertice("Araucária", 23)
  sao_jose_dos_pinhais = Vertice("São José dos Pinhais", 13)
  contenda = Vertice("Contenda", 39)

  porto_uniao.adiciona_adjacente(Adjacente(paulo_frontin,46))
  porto_uniao.adiciona_adjacente(Adjacente(sao_mateus_do_sul,87))
  porto_uniao.adiciona_adjacente(Adjacente(canoinhas,78))

  paulo_frontin.adiciona_adjacente(Adjacente(irati,75))
  paulo_frontin.adiciona_adjacente(Adjacente(porto_uniao,46))

  canoinhas.adiciona_adjacente(Adjacente(porto_uniao,78))
  canoinhas.adiciona_adjacente(Adjacente(mafra,66))
  canoinhas.adiciona_adjacente(Adjacente(tres_barras,12))

  tres_barras.adiciona_adjacente(Adjacente(canoinhas,12))
  tres_barras.adiciona_adjacente(Adjacente(sao_mateus_do_sul,43))

  sao_mateus_do_sul.adiciona_adjacente(Adjacente(tres_barras,43))
  sao_mateus_do_sul.adiciona_adjacente(Adjacente(porto_uniao,87))
  sao_mateus_do_sul.adiciona_adjacente(Adjacente( lapa,60))
  sao_mateus_do_sul.adiciona_adjacente(Adjacente(irati,57))
  sao_mateus_do_sul.adiciona_adjacente(Adjacente(palmeiras,77))

  irati.adiciona_adjacente(Adjacente(palmeiras,75))
  irati.adiciona_adjacente(Adjacente(paulo_frontin,75))
  irati.adiciona_adjacente(Adjacente(sao_mateus_do_sul,57))

  curitiba.adiciona_adjacente(Adjacente(campo_largo,29))
  curitiba.adiciona_adjacente(Adjacente(balsa_nova,51))
  curitiba.adiciona_adjacente(Adjacente(araucaria,37))
  curitiba.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais,15))

  palmeiras.adiciona_adjacente(Adjacente(campo_largo,55))
  palmeiras.adiciona_adjacente(Adjacente(sao_mateus_do_sul,77))
  palmeiras.adiciona_adjacente(Adjacente(irati,75))

  mafra.adiciona_adjacente(Adjacente(canoinhas,66))
  mafra.adiciona_adjacente(Adjacente(lapa,57))
  mafra.adiciona_adjacente(Adjacente(tijucas_do_sul,99))

  campo_largo.adiciona_adjacente(Adjacente(palmeiras,55))
  campo_largo.adiciona_adjacente(Adjacente(balsa_nova,22))
  campo_largo.adiciona_adjacente(Adjacente(curitiba,29))

  balsa_nova.adiciona_adjacente(Adjacente(contenda,19))
  balsa_nova.adiciona_adjacente(Adjacente(curitiba,51))
  balsa_nova.adiciona_adjacente(Adjacente(campo_largo,22))

  lapa.adiciona_adjacente(Adjacente(contenda,26))
  lapa.adiciona_adjacente(Adjacente(sao_mateus_do_sul,60))
  lapa.adiciona_adjacente(Adjacente(mafra,57))

  tijucas_do_sul.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais,49))
  tijucas_do_sul.adiciona_adjacente(Adjacente(mafra,99))

  araucaria.adiciona_adjacente(Adjacente(curitiba,37))
  araucaria.adiciona_adjacente(Adjacente(contenda,18))

  araucaria.adiciona_adjacente(Adjacente(curitiba,15))
  araucaria.adiciona_adjacente(Adjacente(tijucas_do_sul,49))

  contenda.adiciona_adjacente(Adjacente(balsa_nova,19))
  contenda.adiciona_adjacente(Adjacente(araucaria,18))
  contenda.adiciona_adjacente(Adjacente(lapa,26))

grafo = Grafo() #instanciando um objeto do tipo Grafo

"""## Vetor ordenado
Vai apenas ordenar as cidades por ordem de crescente de distancia, do ponto de destino ao ponto final.
"""

import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object) #CRIANDO ARRAY DE TAMANHO E TIPO ESPECIFICADO 

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, vertice):
    if self.ultima_posicao == self.capacidade - 1:  # SE A ULTIMA POSICAO DE VALORES FOR IGUAL A CAPACIDADE -1 (POIS CAPACIDADE COMEÇA A CONTAR DE 1)
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1): #PARA TODO ELEMENTO DE 0 ATÉ O O NUMERO DE ELEMENTOS EM VALORES
      posicao = i  #ATUALIZA A POSICAO
      if self.valores[i].distancia_objetivo > vertice.distancia_objetivo:  #SE A DISTANCIA DO OBJETO PRESENTE EM VALORES FOR MAIOR QUE A DISTANCIA DO OBJETO PASSADO DE ENTRADA NO MÉTODO
        break  #PARA PARAR DE ATUALIZAR A POSICAO, POIS É NESSA POSICAÇÃO QUE IREMOS INSERIR O VERTICE
      if i == self.ultima_posicao: # SE O ÍNDICE DO LOOP FOR IGUAL A ULTIMA POSICAO DA LISTA
        posicao = i + 1  #ADICIONE MAIS UM A POSICAO ONDE SERÁ INSERIDO O VERTICE (NESTE CASO ELE SERÁ INSERIDO NO FINAL DO ARRAY)
    #AFASTAMENTO DOS VALORES PARA A PROXIMA POSICAO CASO NECESSÁRIO
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    #ADICIONANDO O VALOR A SER INSERIDO NA POSICAO ENCONTRADA 
    self.valores[posicao] = vertice
    self.ultima_posicao += 1  #ATUALIZANDO O VALOR DA ULTIMA POSICAO, JA QUE ADICIONAMOS MAIS UM ELEMENTO
#MÉTODO DE IMPRESSÃO DO VETOR   
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].rotulo, ' - ', self.valores[i].distancia_objetivo)

"""## Busca gulosa"""

class Gulosa:
  def __init__(self, objetivo):  #iremos inserir a cidade onde queremos chegar, note que o Objeto do tipo Gulosa também será um Vertice 
    self.objetivo = objetivo
    self.encontrado = False  # por padrao todos os objetos do tipo Gulosa terao esse parâmetro False no inicio

  def buscar(self, atual):  #inicialmente passaremos a cidade atual do ponto de partida, em seguida será feita uma chamada recursiva
    print('-------')
    print('Atual: {}'.format(atual.rotulo)) #como o parâmetro atual passado será um objeto do tipo Vertice, ele pegara o rótulo que é o nome da cidade
    atual.visitado = True #marcará o atributo encontrado da classe Gulosa como Verdadeiro para aquele objeto atual

    if atual == self.objetivo:# caso tenhamos chegado em nosso ponto final
      self.encontrado = True  
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes)) #cria uma lista utilizando o Método VetorOrdenado. len retorna o tamanho do objeto
      for adjacente in atual.adjacentes: # para todo objeto presente dentro da lista adjacentes do objeto Vetor Atual
        if adjacente.vertice.visitado == False:  # se esse adjacente ja ainda nao tiver sido visitado
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente.vertice)  #como o vetor_ordenado foi igualado a um VetorOrdenado ele herda suas caracteristicas, usando entao o método insere
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:  #se o primeiro valor do vetor_ordenado ( menor distancia) for diferente de nada
        self.buscar(vetor_ordenado.valores[0])  # RECURSIVAMENTE chama o próprio método da classe novamente, passando a cidade com menor distancia

busca_gulosa = Gulosa(grafo.curitiba)
busca_gulosa.buscar(grafo.porto_uniao)
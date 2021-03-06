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
  arad = Vertice('Arad', 366) # Cada linha dessas representa um novo objeto do tipo Vertice criado. A distancia  é a distancia da cidade em questao até o destino final em linha reta
  zerind = Vertice('Zerind', 374)
  oradea = Vertice('Oradea', 380)
  sibiu = Vertice('Sibiu', 253)
  timisoara = Vertice('Timisoara', 329)
  lugoj = Vertice('Lugoj', 244)
  mehadia = Vertice('Mehadia', 241)
  dobreta = Vertice('Dobreta', 242)
  craiova = Vertice('Craiova', 160)
  rimnicu = Vertice('Rimnicu', 193)
  fagaras = Vertice('Fagaras', 178)
  pitesti = Vertice('Pitesti', 98)
  bucharest = Vertice('Bucharest', 0)
  giurgiu = Vertice('Giurgiu', 77)
  urziceni = Vertice("Urziceni", 80)
  hirsova = Vertice("Hirsova", 151)
  eforie = Vertice("Eforie", 161)
  vaslui = Vertice("Vaslui", 199)
  lasi = Vertice("Lasi", 226)
  neamt = Vertice("Neamt", 234)

#Ligações entre as cidades:
  arad.adiciona_adjacente(Adjacente(zerind, 75)) # adiciona a lista de ajacentes do Objeto arad do tipo Vertice as cidades adjacentes e a distancia de arad para estas cidades
  arad.adiciona_adjacente(Adjacente(sibiu, 140)) # a distancia é de arad para as cidades adjacentes
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

  urziceni.adiciona_adjacente(Adjacente(bucharest, 85))
  urziceni.adiciona_adjacente(Adjacente(hirsova, 98))
  urziceni.adiciona_adjacente(Adjacente(vaslui, 142))

  hirsova.adiciona_adjacente(Adjacente(urziceni, 98))
  hirsova.adiciona_adjacente(Adjacente(eforie, 86))

  eforie.adiciona_adjacente(Adjacente(hirsova, 86))

  vaslui.adiciona_adjacente(Adjacente(urziceni, 142))
  vaslui.adiciona_adjacente(Adjacente(lasi, 92))

  lasi.adiciona_adjacente(Adjacente(vaslui, 92))
  lasi.adiciona_adjacente(Adjacente(neamt, 87))

  neamt.adiciona_adjacente(Adjacente(lasi, 87))

grafo = Grafo() #instanciando um objeto do tipo Grafo

grafo.arad.mostra_adjacentes()
print("")
grafo.bucharest.mostra_adjacentes()

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

vetor = VetorOrdenado(20)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)
vetor.insere(grafo.zerind)
vetor.insere(grafo.oradea)
vetor.insere(grafo.sibiu)
vetor.insere(grafo.timisoara)
vetor.insere(grafo.mehadia)
vetor.insere(grafo.rimnicu)
vetor.insere(grafo.fagaras)
vetor.insere(grafo.pitesti)
vetor.insere(grafo.giurgiu)

vetor.insere(grafo.urziceni)
vetor.insere(grafo.hirsova)
vetor.insere(grafo.eforie)
vetor.insere(grafo.vaslui)
vetor.insere(grafo.lasi)
vetor.insere(grafo.neamt)

vetor.imprime()

vetor.insere(grafo.lugoj)
vetor.imprime()

var = vetor.valores[0], vetor.valores[0].rotulo

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

busca_gulosa = Gulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.timisoara)
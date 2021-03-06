# -*- coding: utf-8 -*-
"""Cópia de Algoritmos de otimização - calendário de voos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W7pMJId6i1FQECf_V9XiJBAX7bz_7lo0

# Algoritmos de otimização - calendário de voos

## Representação do problema
"""

#TUPLA CLIENTES ----------------------------------------------------------------------------------------
pessoas = [('Lisboa', 'LIS'), 
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

# VOOS DISPONIVEIS ------------------------------------------------------------------------------------
voos = {}
for linha in open('flights.txt'):
  #print(linha)
  #print(linha.split(','))
  origem, destino, saida, chegada, preco = linha.split(',') # onde tiver "," ele vai quebrar a Strig e atribuir cada parte a uma varivel
  voos.setdefault((origem, destino), []) #No dicionário Python, o método setdefault () retorna o valor de uma chave (se a chave estiver no dicionário). Caso contrário, ele insere uma chave com um valor no dicionário.
  voos[(origem, destino)].append((saida, chegada, int(preco)))  #voo[0].append(1,2,3) --> {0:[1,2,3]}

#ALGORITMO IGOR TESTE ---------------------------------------------------------------------------------
def igor_function():
  price = 0
  m_solucao, m_solucaov,solucao,solucaov  = [],[],[],[]
  volta = []
  ida = []
  for i in range(len(pessoas)):
    origem = pessoas[i][1]
    price = voos[origem,destino][0][2]
    for voo in range(len(voos[origem,destino])):
      if voos[origem,destino][voo][2] <= price:
        price = voos[origem,destino][voo][2]
        m_solucao = []
        m_solucao.append(voos[origem,destino][voo])
    ida.append(price)
    solucao.append(m_solucao)
    price = voos[destino,origem][0][2]
    for voo in range(len(voos[destino,origem])):
      if voos[destino,origem][voo][2] <= price:
        price = voos[destino,origem][voo][2]
        m_solucaov = []
        m_solucaov.append(voos[origem,destino][voo])
    volta.append(price)
    solucaov.append(m_solucaov)
  return  solucao, solucaov

igor_function()

#------FUNCAO DE IMPRESSAO-------------------------------------------------------------------------------

def imprimir_voos(agenda):
  id_voo = -1 #colocamos um valor inválido inicialmente
  total_preco = 0 #set da variacao preco
  for i in range(len(agenda) // 2):  # para obtermos apenas 6 laços, ja que sao 6 pessoas
    nome = pessoas[i][0] #pega chave a chave do dicionário pessoas e retorna o valor do índice 0 da lista dentro dessa chave
    origem = pessoas[i][1] #retorna o indice 1 da lista dentro da posicao i do dicionario pessoas (sigla da origem)
    id_voo += 1 #agora incrementamos o id_voo para percorrer a lista agenda e com isso retornar o indice específico da lista dentro do dicionario específico
    ida = voos[(origem, destino)][agenda[id_voo]]
    total_preco += ida[2]     #ida[0] --> horario ida  ida[1]--> horario chegada  ida[2]--> preco
    id_voo += 1 #incremento para pegar o voo de volta
    volta = voos[(destino, origem)][agenda[id_voo]]
    total_preco += volta[2]
    print(f'{nome:10}{origem:4}{ida[0]:>7}-{ida[1]:>5}  R${ida[2]:>4}{volta[0]:>7}-{volta[1]:>5}  R${volta[2]:>4}')
    #print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                #volta[0], volta[1], volta[2])) #JEITO ANTIGO
  print('Preço total: R$', total_preco)


# FITNESS FUNCTION ----------------------------------------------------------------------------------------
def fitness_function(agenda):
  id_voo = -1
  total_preco = 0
  for i in range(len(agenda) // 2):
    origem = pessoas[i][1]
    id_voo += 1
    ida = voos[(origem, destino)][agenda[id_voo]]
    total_preco += ida[2]
    id_voo += 1
    volta = voos[(destino, origem)][agenda[id_voo]]
    total_preco += volta[2]
  
  return total_preco
#------------------------------------------------------------------------------------------------------------
#pip install mlrose --> iNSTALANDO MLROSE
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
 

fitness = mlrose.CustomFitness(fitness_function) #retorna o preco dos voos (temos uma funcao personalizada de fitness)

problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize = False, max_val = 10) 
#(length =tamanho da solucao (12 voos),objeto que criamos acima
#maximize = True -> maximiza o valor retornado, maior preco
#maximize = False -> minimiza o valor retornado, menor preco
#max_val = o algoritmo precisa gerar uma lista com 12 posicoes e o valor maximo é 10
#max_val é a quantidade de voos que temos
#Algoritmo gera uma lista com 12 posicoes e em cada posicao pode variar entre 0 e 9 (10 numeros)


# HILL CLIMB ------------------------------------------------------------------------------------------
"""## Hill climb
subida da encosta (maximos e mínimos global e local)
"""

melhor_solucao, melhor_custo = mlrose.hill_climb(problema, random_state = 1) #random_state -> muda a semente geradora aleatória 
imprimir_voos(melhor_solucao)

# SIMULATED ANNEALING ----------------------------------------------------------------------------------
"""## Simulated annealing"""

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, schedule=mlrose.decay.GeomDecay(init_temp=10000),random_state=1)
imprimir_voos(melhor_solucao)

# ALGORITMO GENÉTICO ----------------------------------------------------------------------------------
"""## Algoritmo genético"""

melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2,random_state=1)
#individuos -> cada solucao é um individo
#Cromossomo -> conjunto de todos os voos [1,2,4,5,8,9,5,6,2]
#Gene -> cada voo individual da solucao
#avaliar populucao -> aplicar a fitness function
imprimir_voos(melhor_solucao)


# SIMULATED ANNEALING OTIMIZADA IGOR ------------------------------------------------------------------------
"""## Simulated annealing OTIMIZADA BY IGOR
Tempera simulado -> processo de aquecer metal e deixá-lo esfriar lentamente
"""

#REALIZEI ALGUMAS OTIMIZAÇÕES
teste_igor_custo = [] #adicionei uma lista de teste
teste_igor_solucao = [] #adicionei uma lista de teste
for i in range(700): #CRIEI ESSE LAÇO PARA ALTERAR O VALOR DE random_state
  melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema,  schedule=mlrose.decay.GeomDecay(init_temp=10000), random_state=i)
#começa com uma solução aleatória, sem o random_state chega em valores melhores
#decay.GeomDecay ->decaimento Geometrico
#decay.ArithDecay -> decaimento Aritimético
#decay.ExpDecay -> Decaimento Exponencial
#init_temp = temperatura inicial -> quanto maior, maior o numero de interacoes
  teste_igor_custo.append(melhor_custo) # A LISTA CRIADA VAI RECEBER O MELHOR CUSTO DE CADA INTERAÇÃO DO FOR
  teste_igor_solucao.append(melhor_solucao)
melhor_valor_igor = min(teste_igor_custo) #EXTRAIO O MENOR VALOR DA LISTA
melhor_random_state = teste_igor_custo.index(melhor_valor_igor)
melhor_solucao_igor = teste_igor_solucao[melhor_random_state]
print(melhor_random_state,melhor_valor_igor,melhor_solucao_igor )

imprimir_voos(melhor_solucao_igor)
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np

# Criando uma lista de coordenadas das cidades:
coords_list = [(1, 1),(4 , 2),(5 ,2 ),(6 , 4),(4 , 4),(3 , 6),(1 , 5),(2 , 3),]

# Inicializar o objeto de função de fitness usando coords_list
fitness_coords = mlrose.TravellingSales(coords = coords_list)

# Criando uma lista de distancia entre os pares de cidades( A u B  = B u A)
dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426),
             (0, 5, 5.3852), (0, 6, 4.0000), (0, 7, 2.2361), (1, 2, 1.0000),
             (1, 3, 2.8284), (1, 4, 2.0000), (1, 5, 4.1231), (1, 6, 4.2426),
             (1, 7, 2.2361), (2, 3, 2.2361), (2, 4, 2.2361), (2, 5, 4.4721),
             (2, 6, 5.0000), (2, 7, 3.1623), (3, 4, 2.0000), (3, 5, 3.6056),
             (3, 6, 5.0990), (3, 7, 4.1231), (4, 5, 2.2361), (4, 6, 3.1623),
             (4, 7, 2.2361), (5, 6, 2.2361), (5, 7, 3.1623), (6, 7, 2.2361)]
   # OBS --> (0, 1, 3.2623) --> (cidade índice 0, cidade índice 1, distância)

# Inicializar o objeto de função de fitness usando coords_list
fitness_dists = mlrose.TravellingSales(distances = dist_list)   

# Definir objeto de problema de otimização
problem_fit = mlrose.TSPOpt(length = 8, fitness_fn = fitness_coords, maximize=False)
# length = número de cidades
# fitness_fn = neste caso usaremos as coordenadas
# maximize = queremos minimizar (menor percurso)

# No caso do nosso exemplo, se escolhermos especificar uma lista de coordenadas, no lugar de um objeto de função de aptidão, podemos inicializar nosso objeto de problema de otimização como:

# Criando uma lista de coordenadas das cidades:
#coords_list = [(1, 1),(4 , 2),(5 ,2 ),(6 , 4),(4 , 4),(3 , 6),(1 , 5),(2 , 3),]

# Inicializar o objeto de função de fitness usando coords_list
#problem_no_fit = mlrose.TSPOpt(length = 8, coords = coords_list, maximize=False)

#Desta vez, suponha que desejamos usar os algoritmos genéticos com as configurações de parâmetro padrão de um tamanho de população (pop_size) de 200, uma probabilidade de mutação (mutation_prob) de 0,1, um máximo de 10 tentativas por etapa (max_attempts) e sem limite de número total máximo de iterações do algoritmo (max_iters). Isso retorna a seguinte solução:

# Resolva o problema usando o algoritmo genético
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
print(best_state)
print(best_fitness)

# Resolva o problema usando o algoritmo genético
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)

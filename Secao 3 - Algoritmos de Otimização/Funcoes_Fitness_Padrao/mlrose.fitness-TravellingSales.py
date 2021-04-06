import numpy as np

class TravellingSales:
    """Função de aptidão para o problema de otimização do caixeiro viajante. 
    Avalia a aptidão de um passeio de n nós, representado pelo vetor de estado 
    : math:` x`, dando a ordem em que os nós são visitados, como a distância total percorrida no passeio (incluindo a distância percorrida entre o nó final no vetor de estado e o primeiro nó no vetor de estado 
    durante o trecho de retorno do passeio). Cada nó deve ser visitado exatamente uma vez para um passeio ser considerado válido. 

    Parâmetros 
    - --------- 
    coords: lista de pares, padrão: Nenhum 
        Lista ordenada das coordenadas (x, y) de todos os nós (onde o elemento i
        fornece as coordenadas do nó i). Isso pressupõe que a viagem entre 
        todos os pares de nós é possível. Se este não for o caso, use 
        : code: `distances` em seu lugar. 

    distâncias: lista de triplos, padrão: Nenhum 
        Lista fornecendo as distâncias, d, entre todos os pares de nós, uev, para os 
        quais a viagem é possível, com cada item da lista no formulário (u, v, d). 
        A ordem dos nós não importa, então (u, v, d) e (v, u, d) são 
        considerados iguais. Se um par estiver faltando na lista, 
        presume 
- se que a viagem entre os dois nós não é possível. Este         argumento é ignorado se coords não for: code: `None`. 

    Exemplos 
    --------
    .. realce :: python 
    .. code-block :: python 

        >>> import mlrose 
        >>> import numpy como np 
        >>> coords = [(0, 0), (3, 0), (3, 2), (2, 4), (1, 3)] 
        >>> dists = [(0, 1, 3), (0, 2, 5), (0, 3, 1), (0, 4, 7), (1, 3, 6), 
                     (4, 1, 9), (2, 3, 8), (2, 4, 2), (3, 2, 8), (3, 4, 4)] 
        >> > fitness_coords = mlrose.TravellingSales (coords = coords) 
        >>> state = np.array ([0, 1, 4, 3, 2]) 
        >>> fitness_coords.evaluate (state) 
        13,86138 ... 
        >>> fitness_dists = mlrose.TravellingSales (distances = dists) 
        >>> fitness_dists.evaluate(state) 
        29 

    Nota 
    ----
    1. A função de fitness TravellingSales é adequada para uso em 
       problemas de otimização de 
caixeiro viajante (tsp) * apenas *.     
2. É necessário especificar pelo menos um dos seguintes: code: `coords` e 
       : code:` distances` ao inicializar um objeto de função de aptidão TravellingSales . 
    """

    def __init__(self, coords=None, distances=None):

        if coords is None and distances is None:
            raise Exception("""At least one of coords and distances must be"""
                            + """ specified.""")

        elif coords is not None:
            self.is_coords = True
            path_list = []
            dist_list = []

        else:
            self.is_coords = False

            # Remove any duplicates from list
            distances = list({tuple(sorted(dist[0:2]) + [dist[2]]) for dist in distances})
            # o dicionario elimina as chaves duplicadas
            # sorted ->ordena os valores de cada item da lista distances

            # Split into separate lists
            node1_list, node2_list, dist_list = zip(*distances)
        
            #A zip()função retorna um objeto zip, que é um iterador de tuplas em que o primeiro item em cada iterador passado é pareado e, em seguida, o segundo item em cada iterador passado é pareado etc.
            # a = ("John", "Charles", "Mike")
            # b = ("Jenny", "Christy", "Monica", "Vicky")
            # x = zip(a, b)
            # x-> (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
            if min(dist_list) <= 0:
                raise Exception("""The distance between each pair of nodes"""
                                + """ must be greater than 0.""")
            if min(node1_list + node2_list) < 0:
                raise Exception("""The minimum node value must be 0.""")

            if not max(node1_list + node2_list) == \
                    (len(set(node1_list + node2_list)) - 1):
                raise Exception("""All nodes must appear at least once in"""
                                + """ distances.""")
                #set() retorna:  
                # um conjunto vazio se nenhum parâmetro for passado
                #um conjunto construído a partir do parâmetro iterável fornecido

            path_list = list(zip(node1_list, node2_list))

        self.coords = coords
        self.distances = distances
        self.path_list = path_list
        self.dist_list = dist_list
        self.prob_type = 'tsp'

    def evaluate(self, state):
        """Evaluate the fitness of a state vector.

        Parameters
        ----------
        state: array
            State array for evaluation. Each integer between 0 and
            (len(state) - 1), inclusive must appear exactly once in the array.

        Returns
        -------
        fitness: float
            Value of fitness function. Returns :code:`np.inf` if travel between
            two consecutive nodes on the tour is not possible.
        """

        if self.is_coords and len(state) != len(self.coords):
            raise Exception("""state must have the same length as coords.""")

        if not len(state) == len(set(state)):
            raise Exception("""Each node must appear exactly once in state.""")

        if min(state) < 0:
            raise Exception("""All elements of state must be non-negative"""
                            + """ integers.""")

        if max(state) >= len(state):
            raise Exception("""All elements of state must be less than"""
                            + """ len(state).""")

        fitness = 0

        # Calculate length of each leg of journey
        for i in range(len(state) - 1):
            node1 = state[i]
            node2 = state[i + 1]

            if self.is_coords:
                fitness += np.linalg.norm(np.array(self.coords[node1])
                                          - np.array(self.coords[node2]))
            else:
                path = (min(node1, node2), max(node1, node2))

                if path in self.path_list:
                    fitness += self.dist_list[self.path_list.index(path)]
                else:
                    fitness += np.inf

        # Calculate length of final leg
        node1 = state[-1]
        node2 = state[0]

        if self.is_coords:
            fitness += np.linalg.norm(np.array(self.coords[node1])
                                      - np.array(self.coords[node2]))
        else:
            path = (min(node1, node2), max(node1, node2))

            if path in self.path_list:
                fitness += self.dist_list[self.path_list.index(path)]
            else:
                fitness += np.inf

        return fitness


    def get_prob_type(self):
        """ Return the problem type.

        Returns
        -------
        self.prob_type: string
            Specifies problem type as 'discrete', 'continuous', 'tsp'
            or 'either'.
        """
        return self.prob_type

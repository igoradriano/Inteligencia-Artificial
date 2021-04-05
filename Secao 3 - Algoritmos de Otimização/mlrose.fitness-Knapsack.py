import numpy as np
class Knapsack:
    """Função de fitness para problema de otimização de mochila. Dado um conjunto de n itens, onde o item i tem peso conhecido: math:` w_ {i} `e valor conhecido : math:` v_ {i} `; e máximo capacidade da mochila,: math: `W`, a função de aptidão da mochila avalia a adequação de um vetor de estado     : matemática:` x = [x_ {0}, x_ {1}, \\ ldots, x_ {n-1}] ` como:

    .. math :: 
        Fitness (x) = \\ sum_ {i = 0} ^ {n-1} v_ {i} x_ {i}, \\ text {if} 
        \\ sum_ {i = 0} ^ {n -1} w_ {i} x_ {i} \\ leq W, \\ texto {e 0, caso contrário,}

    onde: math: `x_ {i}` denota o número de cópias do item i incluídas na mochila.

    Parâmetros 
    ---------- 
    pesos: lista 
        Lista de pesos para cada um dos n itens.

    valores: lista 
        Lista de valores para cada um dos n itens.

    max_weight_pct: float, default: 0,35 
        Parâmetro usado para definir a capacidade máxima da mochila (W) como uma porcentagem do total da lista de pesos (: math: `W =` max_weight_pct: math: `\\ times` total_weight).

    Exemplo 
    ------- 
    .. realce :: python
     .. bloco de código :: python

        >>> import mlrose 
        >>> import numpy como np 
        >>> pesos = [10, 5, 2, 8, 15] 
        >>> valores = [1, 2, 3, 4, 5] 
        >>> max_weight_pct = 0,6 
        >>> fitness = mlrose.Knapsack(pesos, valores, max_weight_pct) 
        >>> state = np.array ([1, 0, 2, 1, 0]) 
        >>> fitness.evaluate(state) 
        11

    Nota 
    ---- 
    A função de adequação da mochila é adequada para uso em problemas de otimização de estado discreto * apenas *.
    """

    def __init__(self, weights, values, max_weight_pct=0.35):

        self.weights = weights
        self.values = values
        self._w = np.ceil(np.sum(self.weights)*max_weight_pct) #soma todos os elementos da lista pesos, multiplica pela peso máximo depois arredonda para cima
        self.prob_type = 'discrete'

        if len(self.weights) != len(self.values):
            raise Exception("""The weights array and values array must be"""
                            + """ the same size.""")

        if min(self.weights) <= 0:
            raise Exception("""All weights must be greater than 0.""")

        if min(self.values) <= 0:
            raise Exception("""All values must be greater than 0.""")

        if max_weight_pct <= 0:
            raise Exception("""max_weight_pct must be greater than 0.""")

    def evaluate(self, state):
        """Evaluate the fitness of a state vector.

        Parameters
        ----------
        state: array
            State array for evaluation. Must be the same length as the weights
            and values arrays.

        Returns
        -------
        fitness: float
            Value of fitness function.
        """

        if len(state) != len(self.weights):
            raise Exception("""The state array must be the same size as the"""
                            + """ weight and values arrays.""")

        # Calcule o peso total e o valor da mochila 
        total_weight = np.sum(state*self.weights)
        total_value = np.sum(state*self.values)

        # Permitir restrição de peso
        if total_weight <= self._w:
            fitness = total_value
        else:
            fitness = 0

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



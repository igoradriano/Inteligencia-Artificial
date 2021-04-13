import numpy as np
from FuncoesComuns import tail, head, max_run
class FlipFlop:
    """Função de aptidão para o problema de otimização de flip-flop. Avalia a aptidão de um vetor de estado: math:` x` como o número total de pares de elementos consecutivos de: math: `x`, (: math:` x_ {i} `e: math:` x_ {i + 1} `) ;  onde: math:` x_ {i} \\ neq x_ {i + 1} `. 

    Exemplo 
    ------- 
    .. destaque :: python 
    .. code-block :: python 

        >>> import mlrose 
        >>> import numpy as np 
        >>> fitness = mlrose.FlipFlop () 
        >>> state = np.array ([0, 1, 0, 1, 1 , 1, 1]) 
        >>> fitness.evaluate(state) 
        Resp: 3 # mudou de estado 3 vezes, seja de 0 para 1 ou de 1 para zero;

    Nota 
    ----
    A função de fitness Flip Flop é adequada para uso em problemas de otimização de estado discreto * apenas *.    
    """

    def __init__(self):

        self.prob_type = 'discrete'

    def evaluate(self, state):
        """Avaliar a adequação de um vetor de estado. 

        Parâmetros 
        ---------- 
        state: array Matriz de estados para avaliação. 

        Retorna 
        ------- 
        fitness: float -  Valor da função de aptidão. 
        """

        fitness = 0
        #AVALIA A MUDANÇA DE ESTADO
        for i in range(1, len(state)):
            if state[i] != state[i - 1]: # se o estado atual for diferente do anterior
                fitness += 1

        return fitness


    def get_prob_type(self):
        """ Retorna o tipo de problema. 

        Retorna 
        ------- 
        self.prob_type: string 
            Especifica o tipo de problema como 'discreto', 'contínuo', 'tsp' 
            ou 'qualquer um (either)'. 
        """
        return self.prob_type


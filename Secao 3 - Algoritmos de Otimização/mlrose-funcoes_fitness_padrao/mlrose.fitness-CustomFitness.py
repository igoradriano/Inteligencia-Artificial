class CustomFitness:
    """Classe para gerar sua própria função de fitness. 

    Parâmetros 
    ---------- 
    fitness_fn: 
        função que pode ser chamada para calcular a aptidão de um estado com a assinatura        
         : code:` fitness_fn (state, ** kwargs) `. 

    problem_type: string, default: 'qualquer' 
        Especifica o tipo de problema como 'discreto', 'contínuo', 'tsp' ou 'qualquer um' 
        (denotando discreto ou contínuo). 

    kwargs: argumentos 
        adicionais Parâmetros adicionais a serem passados ​​para o fitness função. 

    Exemplo 
    ------- 
    .. destaque :: python 
    .. bloco de código :: python 

        >>> import mlrose
        >>> import numpy as np
        >>> def cust_fn(state, c): return c*np.sum(state)
        >>> kwargs = {'c': 10}
        >>> fitness = mlrose.CustomFitness(cust_fn, **kwargs)
        >>> state = np.array([1, 2, 3, 4, 5])
        >>> fitness.evaluate(state)
        150
    """

    def __init__(self, fitness_fn, problem_type='either', **kwargs):
        #**kwargs -> pode ser qualquer tipo de chave para o dicionários ( posso passar um desconto ou uma distancia, desde que eu tenha condicionais para entrada desses valores)
        if problem_type not in ['discrete', 'continuous', 'tsp', 'either']:
            raise Exception("""problem_type does not exist.""")
        self.fitness_fn = fitness_fn
        self.problem_type = problem_type
        self.kwargs = kwargs

    def evaluate(self, state):
        """Evaluate the fitness of a state vector.

        Parameters
        ----------
        state: array
            State array for evaluation.

        Returns
        -------
        fitness: float
            Value of fitness function.
        """

        fitness = self.fitness_fn(state, **self.kwargs)
        return fitness


    def get_prob_type(self):
        """ Return the problem type.

        Returns
        -------
        self.prob_type: string
            Specifies problem type as 'discrete', 'continuous', 'tsp'
            or 'either'.
        """
        return self.problem_type
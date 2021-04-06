import numpy as np
from FuncoesComuns import tail, head, max_run
class ContinuousPeaks:
    """Função de aptidão para o problema de otimização de picos contínuos. Avalia a aptidão de um vetor de estado n-dimensional: matemática:` x`, dado o parâmetro T, como:

    .. math :: 
        Fitness (x, T) = \\ max (max \\ _ run (0, x), max \\ _ run (1, x)) + R (x, T)

    Onde:

    *: math: `max \\ _ run (b, x)` é o comprimento da execução máxima de b's em: math: `x`; 
    *: math: `R (x, T) = n`, if (: math:` max \\ _ run (0, x)> T` e : math: `max \\ _ run (1, x)> T` ); e 
    *: matemática: `R (x, T) = 0`, caso contrário.

    Parâmetros 
    ---------- 
    t_pct: float, padrão: 0.1 
        Parâmetro de limite (T) para função de aptidão de picos contínuos, 
        expresso como uma porcentagem da dimensão do espaço de estado, n (ou seja : matemática: `T = t_ pct} \\ vezes n`).

    Exemplo 
    ------- 
    .. realce :: python
     .. bloco de código :: python

        >>> import mlrose 
        >>> import numpy como np 
        >>> fitness = mlrose.ContinuousPeaks (t_pct = 0,15) 
        >>> state = np.array ([0, 0, 0, 1, 0, 0, 0, 0 , 0, 1, 1, 1]) 
        >>> fitness.evaluate(state) 
        17

    Nota 
    ---- 
    A função de aptidão de Picos Contínuos é adequada para uso em problemas de otimização de string de bits (estado discreto com: code: `max_val = 2`) * apenas *.
    """

    def __init__(self, t_pct=0.1):

        self.t_pct = t_pct
        self.prob_type = 'discrete'

        if (self.t_pct < 0) or (self.t_pct > 1):
            raise Exception("""t_pct must be between 0 and 1.""")

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
        _n = len(state)
        _t = np.ceil(self.t_pct*_n)

        # Calculate length of maximum runs of 0's and 1's
        max_0 = max_run(0, state)
        max_1 = max_run(1, state)

        # Calculate R(X, T)
        if (max_0 > _t and max_1 > _t):
            _r = _n
        else:
            _r = 0

        # Evaluate function
        fitness = max(max_0, max_1) + _r

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



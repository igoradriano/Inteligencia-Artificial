import numpy as np
from FuncoesComuns import tail, head, max_run
class SixPeaks:
    """Função de aptidão para o problema de otimização Six Peaks. Avalia a 
    aptidão de um vetor de estado n-dimensional: matemática:` x`, dado o parâmetro T, como:

    .. math :: 
        Fitness (x, T) = \\ max (tail (0, x), head (1, x)) + R (x, T)

    Onde:

    *: math: `tail (b, x)` é o número de b's finais em: math: `x`; 
    *: math: `head (b, x)` é o número de b's iniciais em: math: `x`; 
    *: math: `R (x, T) = n`, if (: math:` tail (0, x)> T` e 
      : math: `head (1, x)> T`) or (: math: `cauda (1, x)> T` e 
      : matemática:` cabeça (0, x)> T`); e 
    *: matemática: `R (x, T) = 0`, caso contrário.

    Parâmetros 
    ---------- 
    t_pct: float, padrão: 0.1 
        Parâmetro de limite (T) para a função de aptidão Six Peaks, expresso como 
        uma porcentagem da dimensão do espaço de estado, n (ou seja,
         : matemática: `T = t_ { pct} \\ vezes n`).

    Exemplo 
    ------- 
    .. destaque :: python
     .. bloco de código :: python

        >>> import mlrose 
        >>> import numpy como np 
        >>> fitness = mlrose.SixPeaks (t_pct = 0,15) 
        >>> state = np.array ([0, 0, 0, 1, 0, 1, 1, 0 , 1, 1, 1, 1]) 
        >>> aptidão.avaliar (estado) 
        12

    Referências 
    ---------- 
    De Bonet, J., C. Isbell e P. Viola (1997). MIMIC: Encontrando Ótimos por estimativa de Densidades de Probabilidade. Em * Advances in Neural Information 
    Processing Systems * (NIPS) 9, pp. 424–430.

    Nota 
    ---- 
    A função de adequação Six Peaks é adequada para uso em problemas de otimização  de string de bits (estado discreto com: code: `max_val = 2`) * apenas *.  
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

        # Calculate head and tail values
        head_0 = head(0, state)
        tail_0 = tail(0, state)
        head_1 = head(1, state)
        tail_1 = tail(1, state)

        # Calculate R(X, T)
        _r = 0
        _max_score = max(tail_0, head_1)
        if tail_0 > _t and head_1 > _t:
            _r = _n
        elif tail_1 > _t and head_0 > _t:
            _r = _n
            _max_score = max(tail_1, head_0)

        # Evaluate function
        fitness = _max_score + _r

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

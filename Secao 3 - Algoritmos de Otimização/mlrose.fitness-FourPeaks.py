import numpy as np
from FuncoesComuns import tail, head, max_run
class FourPeaks:
    """Função de aptidão para o problema de otimização de quatro picos. Avalia a aptidão de um vetor de estado n-dimensional: math:` x`, dado o parâmetro T, como: 

    .. math :: 
        Fitness (x, T) = \ \ max (tail (0, x), head (1, x)) + R (x, T) 

    onde: 

    *: math: `tail (b, x)` é o número de b's finais em: math: `x `; 
    *: math:` head (b, x) `é o número de b's iniciais em: math:` x`; 
    *: math: `R (x, T) = n`, se: math:` tail ( 0, x)> T` e 
      : math: `head (1, x)> T`; e 
    *: math:` R (x, T) = 0`, caso contrário. 

    Parâmetros 
    --------- - 
    t_pct: float, padrão: 0,1
        Parâmetro de limite (T) para a função de adequação de Quatro Picos, expresso como uma porcentagem da dimensão do espaço de estados, n (isto é : matemática: `T = t_ {pct} \\ vezes n`). 

    Exemplo 
    ------- 
    .. highlight :: python 
    .. code-block :: python 

        >>> import mlrose 
        >>> import numpy as np 
        >>> fitness = mlrose.FourPeaks(t_pct = 0.15) 
        >>> state = np.array ([1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0]) 
        >>> fitness.evaluate(state) 
        Rep: 16 

    Referências 
    ------- --- 
    De Bonet, J., C. Isbell e P. Viola (1997). MIMIC: Encontrando Ótimos por Estimativa de Densidades de Probabilidade.
    Processing Systems * (NIPS) 9, pp. 424–430. 

    Nota 
    ---- 
    A função de aptidão Four Peaks é adequada para uso em problemas de otimização de string de bits (estado discreto com: code: `max_val = 2`) *apenas*.     
    """

    def __init__(self, t_pct=0.1):

        self.t_pct = t_pct
        self.prob_type = 'discrete'

        if (self.t_pct < 0) or (self.t_pct > 1):
            raise Exception("""t_pct must be between 0 and 1.""")


    def evaluate(self, state):
        """Avalia a adequação de um vetor de estado. 

        Parâmetros 
        ---------- 
        state: array Matriz de estado para avaliação. 

        Retorna 
        ------- 
        fitness: float. Valor da função de adequação. 
        """
        _n = len(state)
        _t = np.ceil(self.t_pct*_n)  #A função np.ceil() arredonda os valores do array para cima.
        #_t = t_pc * tamanho do vetor -> arredondado para cima

        # Calcular os valores da cabeça e da cauda 
        tail_0 = tail(0, state) #quantas vezes 0 se repete seguidamente
        head_1 = head(1, state) #quantas vezes 1 se repete seguidamente

        # Calcule R (X, T) 
        if (tail_0 > _t and head_1 > _t): # se tanto a calda quanto a cabeça forem maiores que _t(tantos por cento o tamanho do vetor)
            _r = _n # se satisfação for atendida, _r recebe o tamanho do vetor
        else:
            _r = 0

        # Evaluate function
        fitness = max(tail_0, head_1) + _r

        return fitness


    def get_prob_type(self):
        """ Retorna o tipo de problema. 

        Retorna 
        ------- 
        self.prob_type: string 
            Especifica o tipo de problema como 'discreto', 'contínuo', 'tsp' 
            ou 'qualquer um'. 
        """
        return self.prob_type

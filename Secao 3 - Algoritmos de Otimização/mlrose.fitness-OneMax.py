"" "Classes para definir funções de fitness." "" 

import numpy as np
from FuncoesComuns import tail, head, max_run

class OneMax:
    """Função de adequação para o problema de otimização One Max. Avalia a adequação de um vetor de estado n-dimensional: matemática:` x = [x_ {0}, x_ {1}, \\ ldots, x_ {n-1 }] `como:

    .. math::
        Fitness(x) = \\ sum_ {i = 0} ^ {n-1} x_ {i}

    Example
    -------
    .. highlight:: python
    .. code-block:: python

        >>> import mlrose
        >>> import numpy as np
        >>> fitness = mlrose.OneMax()
        >>> state = np.array([0, 1, 0, 1, 1, 1, 1])
        >>> fitness.evaluate(state)
        Resp: 5

    Nota 
    ----- 
    A função de fitness One Max é adequada para uso tanto discreta como problemas de otimização de estado contínuo. 
    """
    # Construtor da Classe One Max
    def __init__(self):

        self.prob_type = 'either'  #either = 'qualquer um'

    def evaluate(self, state):
        """Avalia a adequação de um vetor de estado. 

        Parâmetros 
        ---------- 
        state: array Matriz de estados para avaliação. 

        Retorna 
        ------- 
        fitness: float - Valor da função de aptidão. 
        """

        fitness = np.sum(state)
        return fitness
    """ np.sum --> Soma dos elementos da matriz em um determinado eixo.
    Ex: np.sum( a , axis = None , dtype = None , out = None , keepdims = <nenhum valor> , inicial = <nenhum valor> , onde = <nenhum valor> )

    Parâmetros:
    a: array_like: 
        Elementos a serem somados.

    axis: Nenhum ou int ou tupla de ints, (opcional):
        Eixo ou eixos ao longo dos quais uma soma é realizada. O padrão, axis = None, somará todos os elementos da matriz de entrada. Se o eixo for negativo, ele conta do último ao primeiro eixo.
        Novo na versão 1.7.0. - Se o eixo for uma tupla de ints, uma soma será executada em todos os eixos especificados na tupla, em vez de um único eixo ou todos os eixos como antes.
    
    dtype: dtype, (opcional):
        O tipo da matriz retornada e do acumulador em que os elementos são somados. O dtype de 'a' é usado por padrão, 'a' menos que a tenha um dtype inteiro com menos precisão do que o inteiro padrão da plataforma. Nesse caso, se 'a' for assinado, o inteiro da plataforma será usado, enquanto se 'a' não tiver sinal, será usado um inteiro sem sinal com a mesma precisão do inteiro da plataforma.
    
    out: ndarray, (opcional):
        Matriz de saída alternativa na qual colocar o resultado. Ele deve ter o mesmo formato da saída esperada, mas o tipo dos valores de saída será convertido, se necessário.

    keepdims: bool, (opcional):
        Se for definido como True, os eixos que são reduzidos são deixados no resultado como dimensões com tamanho um. Com esta opção, o resultado será transmitido corretamente contra a matriz de entrada.
        Se o valor padrão for passado, o keepdims não será passado para o sum método das subclasses de ndarray, no entanto, qualquer valor não padrão será. Se o método da subclasse não implementar keepdims, quaisquer exceções serão levantadas.

    initial: escalar, (opcional):
        Valor inicial da soma. Veja reduce para detalhes.
        Novo na versão 1.15.0.

    where: array_like de bool, (opcional):
        Elementos a incluir na soma. Veja reduce para detalhes.
        Novo na versão 1.17.0.

Returns: 
    sum_along_axis: ndarray:
        Uma matriz com a mesma forma de 'a' , com o eixo especificado removido. Se 'a' for uma matriz 0-d ou se o eixo for Nenhum, um escalar será retornado. Se um array de saída for especificado, uma referência a out é retornada.

Exemplos:
np.sum([0.5, 1.5]) --> 2.0
np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32) --> 1
np.sum([[0, 1], [0, 5]]) --> 6
np.sum([[0, 1], [0, 5]], axis=0) --> array([0, 6])
np.sum([[0, 1], [0, 5]], axis=1) --> array([1, 5])
np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1) --> array([1., 5.])
np.sum([10], initial=5) --> 15
        """


    def get_prob_type(self):
        """ Retorna o tipo de problema. 

        Retorna 
        ------- 
        self.prob_type: string 
            Especifica o tipo de problema como 'discreto', 'contínuo', 'tsp' 
            ou 'qualquer um'. 
        """
        return self.prob_type


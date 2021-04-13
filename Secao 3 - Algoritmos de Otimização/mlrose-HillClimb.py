import numpy as np 
#from .decay import GeomDecay

def hill_climb(problem, max_iters=np.inf, restarts=0, init_state=None, curve=False, random_state=None):
    """ Use hill climbing padrão para encontrar o ideal para um determinado problema de otimização. 

    Parâmetros 
    ---- ------ 
    problem: objeto de otimização 
        Objeto contendo problema de otimização de função de aptidão a ser resolvido. 
        Por exemplo,: code: `DiscreteOpt ()`,: code: `ContinuousOpt ()` ou
        : código: `TSPOpt ()`. 
    max_iters: int, default: np.inf 
        Número máximo de iterações do algoritmo para cada reinicialização. 
    reinicia: int, padrão: 0 
        Número de reinicializações aleatórias. 
    init_state: array, padrão: Nenhum 
        1-D array Numpy contendo o estado inicial do algoritmo. 
        Se: code: `None`, então um estado aleatório é usado. 
    curva: bool, padrão: Falso 
        Booleano para manter os valores de adequação de uma curva. 
        Se: code: `False`, nenhuma curva é armazenada. 
        Se: code: `True`, um histórico de valores de aptidão é fornecido como um 
        terceiro valor de retorno. 
    random_state: int, default: None
        Se random_state for um inteiro positivo, random_state é a semente usada 
        por np.random.seed (); caso contrário, a semente aleatória não é definida. 

    Retorna 
    ------- 
    best_state: array 
        Numpy array contendo o estado que otimiza a função de fitness. 
    best_fitness: float 
        Valor da função de fitness no melhor estado. 
    fitness_curve: array 
        Numpy array contendo o fitness em cada iteração. 
        Retornado somente se o argumento de entrada: code: `curve` for: code:` True`. 

    Referências 
    ---------- 
    Russell, S. e P. Norvig (2010). * Artificial Intelligence: A Modern 
    Approach *, 3ª edição. Prentice Hall, New Jersey, EUA. 
    """

    if(not isinstance(max_iters, int) and max_iters != np.inf and not max_iters.is_integer() or (max_iters<0)):
        raise Exception("""max_iters deve ser um número inteiro positivo.""")
    if(not isinstance(restarts, int) and not restarts.is_integer() or (restarts < 0)):
        raise Exception("""restarts deve ser um número inteiro positivo.""")
    if init_state is not None and len(init_state) != problem.get_length():
        raise Exception("""init_state deve ser um número inteiro positivo.""")

    """Resumindo para que essa exceção seja lançada = max_iters não pode ser do tipo inteiro, não pode ser infinito, e caso número flutante não pode ser integral(ex: 1.0, 2.0, 4.0, tem que ser quebrado) OU  max_iters deve ser menor que zero.

    isinstance(object, type) -> A isinstance()função retorna True se o objeto especificado for do tipo especificado, caso contrário False.
    Exemplos:
    x = isinstance("Hello", (float, int, str, list, dict, tuple)) --> retorna True
    x = isinstance(5, int) --> Retorna True pois 5 é do tipo int
    -------------------------------------------------------------------------------------------------------
    np.inf --> Representação de ponto flutuante IEEE 754 de infinito (positivo). Use inf porque Inf, Infinity, PINF e infty são aliases para inf. Para mais detalhes, veja inf.
    Verificar se um número é infinito - import math -> math.isinf(variavel))
    ----------------------------------------------------------------------------------------------------------
    is_integer( ) -> Retorne True se a instância flutuante for finita com valor integral e, False caso contrário:
    Ex: 
    (-2.0).is_integer()  --> True
    (3.2).is_integer() --> False
    -----------------------------------------------------------------------------------------------------------
    raise - > palavra-chave é usada para gerar uma exceção."""

    # Inicializa o problema de otimização 
    if isinstance(random_state, int) and random_state > 0:
        np.random.seed(random_state)

    best_fitness = -1*np.inf   #best_fitness = -infinito
    best_state = None
        
    """PARÂMETROS:
    -----------------
    seed : {None, int, array_like}
    opcional Semente aleatória usada para inicializar o gerador de número pseudo-aleatório. Pode se qualquer número inteiro entre 0 e 2 ** 32 -1.  Se seed estiver None, Random State tentará ler os dados 
    /dev/urandom (ou o analógico do Windows) se disponíveis ou a semente do relógio, caso contrário."""

    if curve:  #se existir curve crie uma lista chamada fitness_curve
        fitness_curve = []

    # _ -> é convencional em python para usar para variáveis ​​descartáveis. Apenas indica que a variável de loop não é realmente usada.
    for _ in range(restarts + 1):  
        # Inicializa o problema de otimização 
        if init_state is None:  # se não for passado nenhum estado inicial
            problem.reset() #reseta o objeto problem passado 
        else: #se existir um estd inicial passado
            problem.set_state(init_state) #seta o estado para o estado inicial passado
        
        iters = 0

        while iters


#CABEÇA
def head(_b, _x):
    """Determine o número de b's iniciais no vetor x.     
    
    Parâmetros 
    ---------- 
    b: int - Inteiro para contar no cabeçalho do vetor. 
    x: array -  Vetor de inteiros. 

    Retorna 
    ------- 
    head: int - Número de b's 
    """

    # Inicializar contador
    _head = 0

    # Iterate through values in vector
    for i in _x:
        if i == _b:
            _head += 1
        else:
            break

    return _head

# CALDA
def tail(_b, _x): 
    """Determine o número de b's à direita no vetor x.

    Parâmetros 
    ---------- 
    b: int - Inteiro para contar na cauda do vetor.

    x: array - Vetor de inteiros.

    Retorna 
    ------- 
    tail: int -  Número de b's finais em x. 
    """

    # Inicializar contador
    _tail = 0

    # Repita os valores no vetor 
    for i in range(len(_x)):
        if _x[len(_x) - i - 1] == _b: #começa do ultimo elemento de x até o primeiro
            _tail += 1
        else:
            break

    return _tail


def max_run(_b, _x):
    """Determine o comprimento da execução máxima de b's no vetor x. 

    Parâmetros 
    ---------- 
    b: int -  Inteiro para contagem. 

    x: array - Vetor de inteiros. 

    Retorna 
    ------- 
    max: int -  Comprimento da execução máxima de b's.
    """
    # Inicializar contador
    _max = 0
    run = 0

    #  Iterar através de valores no vetor
    for i in _x: #Conta o máximo de vezes que o número não mudou
        if i == _b:
            run += 1
        else:
            if run > _max:
                _max = run

            run = 0

    if (_x[-1] == _b) and (run > _max):
        _max = run

    return _max
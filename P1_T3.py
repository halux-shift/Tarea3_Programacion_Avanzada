import numpy as np

FACTOR_SALTO = 0.8

def calculo_costo_min_perdidas(
        nodos: int, 
        perdidas_nodo: Sequence[float]
        ) -> Optional[float]:
    
    '''
    Calcula el costo mínimo acumulado de pérdida de potencia hasta
    el nodo N
    
    Args: 
        nodos (int): Número de nodos del alimentador (debe ser >= 0).
        perdidas_nodo (Sequence[float]): Lista de pérdidas de potencia en cada nodo.

    Returns:
        Optional[float]: Costo mínimo acumulado de pérdida de potencia hasta el nodo N.
    '''

    #La cantidad de nodos debe ser mayor o igual a 0
    assert nodos >= 0, "La cantidad de nodos no puede ser negativa"

    # La cantidad de mediciones debe ser mayor o igual a la cantidad de nodos
    assert len(perdidas_nodo) >= nodos, (
        "Hay menos mediciones que nodos en el alimentador"
        )
    
    if nodos == 0:
        return 0.0
    
 

import numpy as np

FACTOR_SALTO = 0.8

def calculo_costo_min_perdidas(
        nodos: int, 
        perdidas_nodo: float
        ) -> float:
    
    '''
    Calcula el costo mínimo acumulado de pérdida de potencia hasta
    el nodo N
    
    Args: 
        nodos (int): Número de nodos del alimentador (debe ser >= 0).
        perdidas_nodo (Sequence[float]): Lista de pérdidas de potencia en cada nodo.

    Returns:
        float: Costo mínimo acumulado de pérdida de potencia hasta el nodo N.
    '''

    #La cantidad de nodos debe ser mayor o igual a 0
    assert nodos >= 0, "La cantidad de nodos no puede ser negativa"

    # La cantidad de mediciones debe ser mayor o igual a la cantidad de nodos
    assert len(perdidas_nodo) >= nodos, (
        "Hay menos mediciones que nodos en el alimentador"
        )
    
    if nodos == 0:
        return 0.0
    
    try: 
        costo = np.zeros(nodos + 1)
        costo [1] = perdidas_nodo[0]

        for nodo in range(2, nodos + 1):
            perdida_actual = perdidas_nodo[nodo - 1]
            costo_consecutivo = costo[nodo - 1] + perdida_actual
            costo_salto = costo[nodo - 2] + FACTOR_SALTO * perdida_actual
            costo[nodo] = min(costo_consecutivo, costo_salto)

    except (TypeError, ValueError) as error:
        print(f"[ERROR] Datos corruptos en las mediciones: {error}")
        return None
    
    return float(costo[nodos])
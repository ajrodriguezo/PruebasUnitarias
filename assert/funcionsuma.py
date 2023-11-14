import logging

# TIPOS || VALOR || FUNCION
#DEBUNG = 10 = debug
#INFO = 20 = info
#WARNING 30 = warning
# ERROR = 40 = error
# CRITICAL = 50 = critical

logging.basicConfig(level=logging.DEBUG,
                    format="%(threadName)s - %(levelname)s - %(asctime)s - Message:%(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                    filename="cursoCodigoFacilito.log",
                    filemode="a"
                    )
# por default siempre se ven los mayores o iguales a 30

def suma_numeros_positivo(n1: int, n2: int)-> int:
    """Permite sumar 2 numero enteros positivos

    Args:
        n1 (int)
        n2 (int)

    Returns:
        int:
    """
    #if n1<0 or n2<0 :
    #    return None
    
    logging.debug('antes de sumar')
    
    try:    
        assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar numeros enteros'
        
        return n1+n2
    
    except AssertionError as error:
        print(error)

    logging.debug('despues de sumar')
        
        

if __name__ == '__main__':
    logging.debug('antes del llamdo')
    
    resultado = suma_numeros_positivo(10,20)
    logging.info(resultado)
    
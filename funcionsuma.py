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
    
    try:    
        assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar numeros enteros'
        
        return n1+n2
    
    except AssertionError as error:
        print(error)
        
        

if __name__ == '__main__':
    resultado = suma_numeros_positivo(10,20)
    print(resultado)
    
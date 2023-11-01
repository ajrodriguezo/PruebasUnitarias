# Docstring

def palindromo (senctence: str) -> bool:
    """Esta funcion permite conocer si un string
    es un palindromo , o no, es decir, que se puede 
    leer igual de  izquierda a derecha que de derecha a izquierda

    Args:
        sentence: string

    Returns:
        bool
    """

    senctence = senctence.lower().replace(' ','')
    return senctence == senctence[::-1]
# Docstring

def palindromo (senctence: str) -> bool:
    """Esta funcion permite conocer si un string
    es un palindromo , o no, es decir, que se puede 
    leer igual de  izquierda a derecha que de derecha a izquierda

    Args:
        sentence: string

    Returns:
        bool
        
    Sepuede poner lo necesario y lo querequieras en el docstring
    pero siempre es mejor utilizar lo estandarizado por la comunidad
    en este caso seguiremos la documentacion de google
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    
    para que este formato quede mejor vamos aktulizar una extencion 
    de VsCode autoDocstring
    
    para eso solo falta poner triple comillas doble sy generar
    
        '''_summary_

    Returns:
        _type_: _description_
    '''
    
    Dentro del docstring podemos generar pruebas para ver que la funcion esta funcionanod
    Se le puede dar cualquier nombre y tenemos que simular que estamos en el shell interactivo de python
    Dando la entrada con:
    
    #>>> funcion(Argumentos)
    #respuesta esperada
    
    Examples:
    
    >>> palindromo('anita lava la tina')
    True
    
    """
    


    senctence = senctence.lower().replace(' ','')
    return senctence == senctence[::-1]
# assert

if __name__ == '__main__':
    
    try:
        assert 5==10 , 'lo sentimos 5 no es igual a 10'
        '''
        if not 5 == 10:
            raise AssertionError('lo sentimos 5 no es igual a 10')
            
        en python es mejor lanzar errores que condicionar
        por eso es mejor la sentencia assert
        '''

        print('El programa continua con su ejecucion ')
    
    except AssertionError as error:
        print(error)
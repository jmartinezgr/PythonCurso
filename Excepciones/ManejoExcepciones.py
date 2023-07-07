from NumerosIdenticosException import NumerosIdenticosException

resultado = None
try:
    a = int(input('Ingresa un numero: '))
    b = int(input('Ingresa otro numero: '))
    if a==b:
        raise NumerosIdenticosException(f'Numeros identicos: {a} = {b}')

    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}')
except ValueError as e:
    print(f'ValueError - Ocurrio un error: {e}')
except NumerosIdenticosException as e:
    print(f'SameValues - Ocurrio un error: {e}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e} - {type(e)}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecucion del bloque finally')

print(resultado)
print('Continuamos...')
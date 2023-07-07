from LaboratorioSeccion1.Domain.Pelicula import Pelicula
from Services.CatalogoPeliculas import CatalogoPeliculas as cp

while True:
    try:
        print("""
OPCIONES
1.Agregar pelicula
2.Listar peliculas
3.Eliminar peliculas
4.Salir
        """)
        opcion = int(input('Ingresa tu opcion (1-4):'))
        if opcion not in (1,2,3,4):
            raise ArithmeticError
        else:
            if opcion == 4:
                print('Terminamos el programa ... ')
                break
            elif opcion == 1:
                nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
                pelicula = Pelicula(nombre_pelicula)
                cp.agregar_pelicula(pelicula)
            elif opcion == 2:
                cp.lista_peliculas()
            else:
                cp.eliminar_peliculas()
    except ValueError as e:
        print('Recuerda ingresar un valor numerico')
    except ArithmeticError as e:
        print('Recuerda ingresar un numero entre 1 y 4')
    except Exception as e:
        print(f'Ha ocurrido un error:{e}')

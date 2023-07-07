import os

class CatalogoPeliculas:
    #Contexto estatico
    ruta_archivo = 'Services\\pelicula.txt'

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf8') as f:
            f.write(f'{pelicula.nombre}\n')

    @classmethod
    def lista_peliculas(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as f:
            print('Catalogo de peliculas'.center(50,'-'))
            print(f.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
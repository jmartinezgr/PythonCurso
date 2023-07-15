import psycopg2

conexion = psycopg2.connect(user='postgres',password='1018224606',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            id_persona=input('Proporciona el valor de id_persona: ')
            cursor.execute('SELECT id_persona, nombre FROM persona WHERE id_persona = %s ',(id_persona,))
            print(cursor.fetchone())
except Exception as e:
    print(f'Ocurrion un error: {e}')
finally:
    conexion.close()

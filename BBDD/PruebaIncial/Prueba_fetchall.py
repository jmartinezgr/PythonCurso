import psycopg2

conexion = psycopg2.connect(user='postgres', password='1018224606', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT id_persona, nombre FROM persona WHERE id_persona IN (%s,%s,%s)',(1,2,3))
            for resultado in cursor.fetchall():
                print(resultado)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

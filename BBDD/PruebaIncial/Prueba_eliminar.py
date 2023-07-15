import psycopg2

conexion = psycopg2.connect(user='postgres', password='1018224606', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            valor = (11,)  # Corrección: eliminar la coma adicional
            cursor.execute('DELETE FROM persona WHERE id_persona = %s', valor)
            registros = cursor.rowcount
            print(f'Registros eliminados = {registros}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

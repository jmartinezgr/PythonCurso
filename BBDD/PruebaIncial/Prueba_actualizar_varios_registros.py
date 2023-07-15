import psycopg2

conexion = psycopg2.connect(user='postgres', password='1018224606', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            valores = (
                ('Adriana','Marin',1),
                ('Isabela','Grisales',2)
            )
            cursor.executemany('UPDATE persona SET nombre=%s, apellido=%s WHERE id_persona=%s',valores)
            #conexion.commit()
            registros = cursor.rowcount
            print(f'Registros actualizados = {registros}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

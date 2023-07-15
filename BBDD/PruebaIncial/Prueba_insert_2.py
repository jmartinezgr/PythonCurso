import psycopg2

conexion = psycopg2.connect(user='postgres', password='1018224606', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            valores = (
                ('Marcos','Cantu','mcantu@gmail.com'),
                ('Angel','Quintana','aquintana@gmail.com'),
                ('Maria','Gonzales','mgonzales@gmail.com')
            )

            cursor.executemany('INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)',valores)
            #conexion.commit()
            registros = cursor.rowcount
            print(f'Registros insertados = {registros}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

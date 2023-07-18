import psycopg2 as bd

conexion = bd.connect(user='postgres', password='1018224606', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores = ('Adriana','Grisales','luzadri0512@gmail.com')
            cursor.execute(sentencia,valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona =  %s'
            valores = ('Katerine','Martinez','ktmartinez@gmail.com',14)
            cursor.execute(sentencia,valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo rollback: {e}')

print('Transaccion terminada, se hizo commit')
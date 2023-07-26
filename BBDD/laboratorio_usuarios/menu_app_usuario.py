from BBDD.laboratorio_usuarios.usuario import Usuario
from BBDD.laboratorio_usuarios.usuario_dao import UsuarioDAO
from BBDD.laboratorio_usuarios.logger_base import log

opcion = None
while opcion !=5:
    print('''
Opciones:
1. Listar usuarios
2. Agregar usuario
3. Modificar usuario
4. Eliminar Usuario
5. Salir
''')
    opcion = int(input('Escribe tu opcion (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var,password=password_var)
        if UsuarioDAO.insertar(usuario) == 1:
            log.info(f'Usuarios insertados exitosamente')
        else:
            log.error('No se ha podido insertar el usuario')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id del usuario a modificar: '))
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(id_usuario_var,username_var,password_var)
        if UsuarioDAO.actualizar(usuario) == 1:
            log.info(f'Se ha actualizado el usuario')
        else:
            log.error('No se ha podido actualizar el usuario')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario_var)
        if UsuarioDAO.eliminar(usuario) == 1:
            log.info('Usuario eliminado con exito')
        else:
            log.error('No se ha podido eliminar el usuario')
else:
    log.info('Salimos de la aplicación')
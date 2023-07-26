from cursor_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDAO:
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s  WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionado usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            cursor.execute(cls._INSERTAR,(usuario.username,usuario.password))
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a modificar: {usuario}')
            cursor.execute(cls._ACTUALIZAR,(usuario.username,usuario.password,usuario.id_usuario))
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar con id de usuario {usuario.id_usuario}')
            cursor.execute(cls._ELIMINAR,(usuario.id_usuario,))
            return cursor.rowcount


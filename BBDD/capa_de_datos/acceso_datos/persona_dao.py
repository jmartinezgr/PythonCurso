from BBDD.capa_de_datos.acceso_datos.conexion import Conexion
from BBDD.capa_de_datos.login.logger_base import log
from BBDD.capa_de_datos.acceso_datos.persona import Persona

class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.info(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.info(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.info(f'Objeto eliminado: {persona}')
                return cursor.rowcount

if __name__ == '__main__':
    #Insertar
    #persona1 = Persona(nombre='Pedro',apellido='Najeda',email='pnajera@gmail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #if(personas_insertadas == 1):
    #    log.info(f'Personas insertadas: {personas_insertadas}')
    #else:
    #    log.error('No se pudo insertar la persona')

    #Actualizar un registro
    #persona1 = Persona(17,'Manuela','Rodriguez','mrodriguez@gmail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #if(personas_actualizadas==1):
    #    log.info(f'Personas actualizadas: {personas_actualizadas}')
    #else:
    #    log.error(f'Error al actualizar personas')

    persona1 = Persona(id_persona=4)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    if(personas_eliminadas==1):
        log.info(f'Personas actualizadas: {personas_eliminadas}')
    else:
        log.error(f'Error al actualizar personas')

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
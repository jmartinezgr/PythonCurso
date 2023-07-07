archivo = open('prueba.txt','r',encoding='utf8')

#print(archivo.readlines())
#Ya no hay lineas que leer
#for linea in archivo:
#   print(linea)


try:
    archivo2 = open('copia.txt','a',encoding='utf8')
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
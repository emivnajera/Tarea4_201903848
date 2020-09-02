import json
import os


#Declaracion de las Listas que Alamcenaran los datos
listaNombres = []
listaEdad = []
listaActivo = []
listaSaldo = []


#Llamado del archivo .json
with open('archivo.json') as data:
    info = json.load(data)

#Llenamos la lista con los registros
for i in info:
    listaNombres.append(i['nombre'])
    listaEdad.append(i['edad'])
    listaActivo.append(i['activo'])
    listaSaldo.append(i['saldo'])
#vericamos la existencia del html
if os.path.exists('Reporte.html'):
            if not os.path.isdir('Personas'):
                os.mkdir('Personas')
            with open('Reporte.html', 'r') as file:
                content = file.read()
                tabla = file.read()
            with open('Reporte.html', 'r') as file:
                content = file.read()
                tabla = file.read()
            cont = 0
            #remplazamos el parrafo vacio en el html
            for i in info:
                content = content.replace('{Elementos}',
                                          '<tr>\n<td><p>{Nombre' + str(cont) + '}</p></td>\n<td><p>{Edad' + str(
                                              cont) + '}</p></td><td><p>{Activo' + str(
                                              cont) + '}</p></td>\n<td><p>{Saldo' + str(
                                              cont) + '}</p></td>\n</tr>\n<b>{Elementos}</b>')
                cont = cont + 1
            content = content.replace('{Elementos}', '')
            con = 0
            #agregamos los elementos de los registros al html
            for i in info:
                content = content.replace('{Nombre' + str(con) + '}', listaNombres[con])
                content = content.replace('{Edad' + str(con) + '}', str(listaEdad[con]))
                content = content.replace('{Activo' + str(con) + '}', str(listaActivo[con]))
                content = content.replace('{Saldo' + str(con) + '}', str(listaSaldo[con]))
                con = con + 1
            #creamos el nuevo html
            with open('RegistroNuevo' + '.html', 'w') as file:
                file.write(content)



                #mensaje de confirmacion
                print('Reporte Generado')
else:
    #mensaje en caso que no exista el html
    print('no existe el archivo')
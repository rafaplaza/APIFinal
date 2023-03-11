from flask import Flask, jsonify, request
import mysql.connector

#Conexión con base de datos:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cochesapi"
)

#Aplicación de servidor:
app = Flask(__name__) 

@app.route('/hello')
def hello_world():
    return 'Hola, mundo!'

# METODO GET: 
@app.route('/coches', methods=['GET'])
def obtener_coches():
    # Crear un cursor y ejecutar una consulta SQL
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM coches")    
    # Obtener los resultados de la consulta
    resultados = mycursor.fetchall()    
    # Crear una lista de diccionarios con los datos de los coches
    coches = []
    for resultado in resultados:
        coche = {
            "id": resultado[0],
            "modelo": resultado[1],
            "año": resultado[2],
            "bastidor": resultado[3],
            "titular": resultado[4]
        }
        coches.append(coche)
    # Devolver los datos en formato JSON
    return jsonify(coches)

#METODO GET para obtener un coche a través de su id:
@app.route('/coches/<int:id>', methods=['GET'])
def obtener_coche(id):
    # Crear un cursor y ejecutar una consulta SQL
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    
    # Obtener el resultado de la consulta
    resultado = mycursor.fetchone()
    
    # Devolver los datos en formato JSON
    if resultado:
        coche = {
            "id": resultado[0],
            "modelo": resultado[1],
            "año": resultado[2],
            "bastidor": resultado[3],
            "titular": resultado[4]
        }
        return jsonify(coche)
    else:
        return jsonify({"mensaje": "Coche no encontrado"}), 404

#METODO POST    
# Ruta para agregar un nuevo coche A TRAVÉS DE INSOMNIA
# Da igual que tengan el mismo nombre por que al tener distintos métodos http no pasa nada
@app.route('/coches', methods=['POST'])

def agregar_coche():

    # print(request.json): es para recibir el dato, recibe las peticiones que me están enviando a través de http   
    # Estos nuevos datos los tengo que volver a enviar desde el POST (json insomnia)
    nuevo_coche = {
        "id": request.json['id'],
        "modelo": request.json['modelo'],  
        "año" : request.json['año'],
        "bastidor": request.json['bastidor'], 
        "titular": request.json['titular'], 
    }
   # Crear un cursor y ejecutar una consulta SQL para insertar los datos
    mycursor = mydb.cursor()
    sql = "INSERT INTO coches (id, modelo, año, bastidor, titular) VALUES (%s, %s, %s, %s, %s)"
    val = (nuevo_coche['id'], nuevo_coche['modelo'], nuevo_coche['año'], nuevo_coche['bastidor'], nuevo_coche['titular'])
    mycursor.execute(sql, val)
    mydb.commit()
    
    # Devolver una respuesta exitosa
    return jsonify({"mensaje": "coche agregado correctamente"})    

#METODO POST
# Ruta para agregar un nuevo coche A TRAVÉS DE LA URL
@app.route('/cochesPost/<int:id>/<modelo>/<int:anio>/<bastidor>/<titular>', methods=['POST'])
def agregar_coche_url(id, modelo, anio, bastidor, titular):
    # Crear un cursor y ejecutar una consulta SQL para insertar los datos
    mycursor = mydb.cursor()
    sql = "INSERT INTO coches (id, modelo, año, bastidor, titular) VALUES (%s, %s, %s, %s, %s)"
    val = (id, modelo, anio, bastidor, titular)
    mycursor.execute(sql, val)
    mydb.commit()
    # Devolver una respuesta exitosa
    return jsonify({"mensaje": "coche agregado correctamente"})

#Método PUT: Sirve para actualizar algo
@app.route('/coches/<int:id>', methods=['PUT'])
def editar_coche(id):
    # Crear un cursor y ejecutar una consulta SQL
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    cocheEncontrado = mycursor.fetchone()
    if cocheEncontrado is None:
        return jsonify({'mensaje': 'Coche no encontrado'}), 404
    
    coche_data = request.get_json()
    nuevo_coche = {
        'id': id,
        'modelo': coche_data.get('modelo', cocheEncontrado[1]),
        'año': coche_data.get('año', cocheEncontrado[2]),
        'bastidor': coche_data.get('bastidor', cocheEncontrado[3]),
        'titular': coche_data.get('titular', cocheEncontrado[4])
    }

    # Construir la consulta UPDATE y ejecutarla
    query = "UPDATE coches SET modelo = %s, año = %s, bastidor = %s, titular = %s WHERE id = %s"
    values = (nuevo_coche['modelo'], nuevo_coche['año'], nuevo_coche['bastidor'], nuevo_coche['titular'], id)
    mycursor.execute(query, values)
    mydb.commit()

    # Devolver el coche actualizado
    return jsonify(nuevo_coche)


#Método PUT para actualizar el titular a través del id con un valor que le pongo en insomnia:
@app.route('/cochesTitular/<int:id>', methods=['PUT'])   
def editar_titular_coche_insomnia(id):
    # Crear un cursor y ejecutar una consulta SQL
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    cocheEncontrado = mycursor.fetchone()
    
    if cocheEncontrado is None:
        return jsonify({'mensaje': 'Coche no encontrado'}), 404
    
    # Obtener el nuevo titular del coche del cuerpo de la petición
    nuevo_titular = request.json.get('titular')

    # Actualizar el coche con el nuevo titular
    query = "UPDATE coches SET titular = %s WHERE id = %s"
    values = (nuevo_titular, id)
    mycursor.execute(query, values)
    mydb.commit()

    # Obtener el coche actualizado y devolverlo en la respuesta
    mycursor.execute("SELECT * FROM coches WHERE id = %s", (id,))
    cocheActualizado = mycursor.fetchone()
    return jsonify(cocheActualizado)


#METODO PUT para que el nuevo titular sea uno que yo introduzca como segundo parámetro en la URL:
#La URL para actualizar el titular del coche a Rafa con ID 123 sería: /coches/123/titular?nuevo_titular=Rafa

@app.route('/coches/<int:id>/titular', methods=['PUT'])
def editar_titular_coche_url(id):
    # Obtener el nuevo titular del coche del parámetro de la URL
    nuevo_titular = request.args.get('nuevo_titular')
    # Crear un cursor y ejecutar una consulta SQL para actualizar el titular del coche
    mycursor = mydb.cursor()
    query = "UPDATE coches SET titular = %s WHERE id = %s"
    values = (nuevo_titular, id)
    mycursor.execute(query, values)
    mydb.commit()

    # Devolver un mensaje de éxito
    return jsonify({'mensaje': f'Titular del coche con ID {id} actualizado correctamente a "{nuevo_titular}"'})
    

# METODO DELETE por su ID
@app.route('/cochesDelete/<int:id>', methods=['DELETE'])
def eliminar_coche(id):
    # Eliminar el coche de la base de datos
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM coches WHERE id = %s", (id,))
    mydb.commit()    
    # Devolver una respuesta exitosa
    return jsonify({"mensaje": "Coche eliminado correctamente"})
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['usuarios']

def agregar_usuario(nombre, edad):
    usuario = {
        'nombre': nombre,
        'edad': edad
    }
    collection.insert_one(usuario)

def obtener_usuarios():
    return collection.find()

if __name__ == '__main__':
    agregar_usuario('Diego', 23)
    agregar_usuario('Branko', 23)
    usuarios = obtener_usuarios()
    for usuario in usuarios:
        print(usuario)


from flask import Flask,request
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)
#para configurar los cors lo hago de la siguiente manera

# Si lo dejamos sin ninguna configuracion adicional lo que va a suceder es que en teoria va a permitir que todos los origenes, todos los metodos y todos os headers sean permitidos
CORS(app=app, 
     methods=['GET','POST','PUT','DELETE'], # que metodos pueden acceder a mi API 
     # si quisieramos que se pueda acceder desde cualquier origen lo hacemos con '*'
     origins=['http://127.0.0.1:5500','http://localhost:5500'], # que dominios pueden acceder a mi API
     allow_headers=['accept','Authorization','content-type']) # que cabeceras pueden acceder a mi API

productos = [
    {
        'id':uuid4(),
        'nombre':'palta fuerte',
        'precio': 7.50,
        'disponibilidad': True
    },
    {
        'id':uuid4(),
        'nombre':'Lechuga carola',
        'precio': 1.50,
        'disponibilidad': True
    },
]

@app.route("/", methods = ["GET"])
def inicio():
    return {"Hello World"},200

@app.route('/productos', methods = ["GET"])
def gestionProductos():
    return {'message': 'Los productos son',
            'content':productos},200
#si voy a recibir un parametro dinamico (que va a cambiar su valor) y esto lo voy a menjar internamente
#los fomratos que puedo parcear son
#string para recibir texto
#int para recibir solo numeros
#float para recibir numeros con decimales
#path para recibir parametros de la url o texto con slashes
#uuid aceptar UUIDs
#al colocar un parceadro si el formato que me envia el cliente no cumple con este coinversion no aceptara lapeticion
#si yo defino un parametro dinamico ese parametro lo tenfo quer 
@app.route('/producto/<uuid:id>', methods = ["GET"])
def gestionProducto(id):
    print(id)
    #tenemos una lista de productos en el cual en cada posicion tenemos un diccionario y una llave llamada id
    #iterear esos productos y vean si existe el producto con determinado id
    #hacer un for con if y else dentro de el
    for producto in productos:
        if producto['id'] == id:
            return {'message': 'El producto es',
                    'content':producto},200
        # elif producto['id'] != id:
        #     return {'message': 'El producto no existe'},404
        
    return {'message': 'El producto no existe'},404

@app.route('/producto', methods = ["POST"])
def crearProducto():
    data = request.get_json() # el get json convierte la data del body a un diccionario si el body es un JSON
    # antes de guardar la informacion en los productos agregarle el id
    data['id'] = uuid4()
    productos.append(data)
    return{
        'message':'Producto creado exitosamente',
        'content':data
    },201

if __name__ == "__main__":
    app.run(debug = True)
from flask import Flask,request
#En request > Donde se almacenara toda la informacion de la peticion actual del cleinte
# Cada vez que el cliente relice una peticion tp0da esa ionmfoprmacion se almacenara en el requst

#__name__ > variable de python que sirve para indicar el nombre del archivo actual o principal esto sirve para que la instancia de Flask solamente corra en el carchivo principal y  asi devitar instancias de Flask en archivos secundarios del proyecto
app = Flask(__name__)

#Si el archivo es el principal el valor de __name__ sera __main__

#Decoradores
#sirve para utilizar un metodo sin la necesidad de modificarlo desde la clase en la cual estamos haciendo la referencia
#GET sirve para devolver
#POST sirve para crear
#PUT sirve para actualizar
@app.route('/', methods=['GET','POST','PUT'])
def inicio():
    #request.method devolvera el metodo HTTP que esta realizando el cliente
    if request.method == 'PUT':
        return{
            'message':'Actualizacion exitosa',
            
        }
    elif request.method == 'GET':
        return{
            'message':'Devolucion exitosa'
        }
    elif request.method == 'POST':
        return{
            'message':'Creacion exitosa'
        }
    print(request.method)


    return{
        'message':'Bienvenido a mi primera API con Flask',
        'content':'Este es otro mensaje'
    }


#levantamos nuestro servidor flask con app.run
app.run(debug = True)
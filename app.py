
from marshmallow import Schema,fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel
from flask import Flask, request
from flask_migrate import Migrate
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

swaggerui = get_swaggerui_blueprint(
   base_url='/documentacion',
   api_url='/static/documentacion.json',
   config={
      'app_name':'API de Usuarios'
   }
)


app = Flask(__name__)
CORS(app=app)
# print(app.config)
# app.config almacenara todas las variables que se utilizan en el proyecto de Flask
# NOTA: No confundir con las variables de entorno!
# ahora agregamos una nueva llave a nuestra variables de configuracion
# dialecto://usuario:contraseña@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/alumnos'
# Inicializar la conexion a nuestra BD
# al momento de pasarle la aplicacion de flask en esta se encontraras la cadena de conexion a la bd
conexion.init_app(app)

Migrate(app=app, db=conexion)

# class UsuarioDTO(Schema):
#    nombre = fields.Str(required =True)
#    apellido = fields.Str()
#    correo = fields.Email(required =True)
#    fechaNacimiento = fields.Date()

class UsuarioModelDTO(SQLAlchemyAutoSchema):
   class Meta:
      model = UsuarioModel



# before_request > se mandara a llamar a esta funcionabilidad antes de cualquier request (peticion)
@app.before_request
def inicializacion():
    # create_all > crea todas las tablas que no se han creado en la base de datos
    conexion.create_all()

@app.route('/usuarios', methods=['GET'])
def gestionarUsuarios():
    resultado = conexion.session.query(UsuarioModel).all()
    validador = UsuarioModelDTO()
    usuarios = validador.dump(resultado, many=True)
    # usuarios=[]
    # for usuario in resultado:
    #     usuarios.append({
    #         'id':usuario.id,
    #         'nombre':usuario.nombre,
    #         'apellido':usuario.apellido,
    #         'correo':usuario.correo,

            # %Y devolvera el a;o en formato de 4 digitos
            # %m devolvera el mes en formato de 2 digitos
            # %m devolvera el dia en formato de 2 digitos
            # %B devolvera el mes en formato de texto
            # %d devolvera el dia en formato de 2 digitos
            # %b devolvera el tes rprimeras letras del mes
        #     'fechaNacimiento':datetime.strftime(usuario.fechaNacimiento, '%Y-%m-%d'),
        # })

    print(resultado)

    return{
        'conent':usuarios
    },200

@app.route('/usuario', methods=['POST'])
def crearUsuario():

 try:
    data = request.get_json()
    # validador = UsuarioDTO()
    validador = UsuarioModelDTO()

    dastaValidada = validador.load(data)

    # print(dastaValidada)
    # return{
    #    'message':None
    # }
    # nuevoUsuario = UsuarioModel(nombre = data.get('nombre'),
    #                             apellido = data.get('apellido'), 
    #                             correo = data.get('correo'), 
    #                             fechaNacimiento = data.get('fechaNacimiento'))
    nuevoUsuario = UsuarioModel(**data)

    # agregar este registro a la base de dastos de manera temporal
    conexion.session.add(nuevoUsuario)

    print('antes del commit: ', nuevoUsuario.id)
    # commit sirve para transacciones y permite que todos los cambios realizados den la base de datos permanezcan de manera persistente
    conexion.session.commit()
    usuarioCreado = validador.dump(nuevoUsuario)

    # usuarioCreado = {
    #     "nombre": nuevoUsuario.nombre,
    #     "apellido": nuevoUsuario.apellido,
    #     "correo": nuevoUsuario.correo,
    #     "fechaNacimiento": nuevoUsuario.fechaNacimiento,
    # }
    print('despues del commit: ',datetime.strftime( nuevoUsuario.id, '%Y-%m-%d'))

    return {
        'message': 'Bienvenido a mi API de usuarios',
        # mostrar el usuario recien creado
        'content': usuarioCreado,
        
    },201
 except Exception as error:
    return {
        'message': 'Error al crear el usuario',
        'error': error
    },500 

@app.route('/usuario/<int:id>', methods=['GET','PUT','DELETE'])
def gestionarUsuario(id):
   if request.method == 'GET':
    usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
    # Si queremos definir que columas utilizar al momento de 
    prueba = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.correo).all()
    print(prueba)

    if usuarioEncontrado is None:
        return {
            'message': 'Usuario no encontrado'
        },404
    
    # ussar el UsuarioModelDTO para devolver la informacion
    validador = UsuarioModelDTO()
    usuario = validador.dump(usuarioEncontrado)
    return { 
        'message': 'Usuario encontrado',
        'content': usuario
    },200
   elif request.method == 'PUT':
      usuarioEncontrado=conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id=id).first()
      if not usuarioEncontrado:
         return{
            'message':'Usuario no existe'
         },404
      validador = UsuarioModelDTO()

      datavalidada = validador.load(request.get_json())
      #uodate usuarios set nombnre = nombre='...', apellido='....' where id=...
      conexion.session.query(UsuarioModel).filter_by(id=id).update(datavalidada)
      conexion.session.commit()
      return{
         'message':'Usuario actualizado exitosamente'
      }
   elif request.method == 'DELETE':
      usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id=id).first()

      if not usuarioEncontrado:
         return{
            'message':'usuario no existe'
         },404
      conexion.session.query(UsuarioModel).filter_by(id=id).delete()
      conexion.session.commit()
      return {'message':'usuario eliminado'},204
   
@app.route('/usuario/deshabilitar/<int:id>', methods=['DELETE'])
def deshabilitarUsuario(id):
    usuarioEncontrado = conexion.session.query(UsuarioModel).with_entities(UsuarioModel.id).filter_by(id=id).first()
    if not usuarioEncontrado:
         return{
            'message':'usuario no existe'
         },404
    conexion.session.query(UsuarioModel).filter_by(id=id).update({'activo'==False})
    conexion.session.commit()
    return{
       'message':'Usuario inhabilitado exitosamente'
    }
   

 
    
    
@app.route('/')
def inicial():
    return 'Bienvenido a mi API de usuarios'


if __name__ == '__main__':
    app.run(debug=True)

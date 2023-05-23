from flask import Blueprint , flash , g , redirect , render_template , request , session , url_fo
from alchemyClasses.insumo import insumo
from models.modelo_insumo import insumo, consultar_insumo

consulta_insumo_blueprint = Blueprint('consulta_de_insumo' , _name_, url_prefix = 'consulta_de_insumo')

@consulta_insumo_blueprint.route('/', methods =['GET'])
def consulta_insumo():
  if request.method == 'GET':
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    cantidad = request.form['cantidad']
    ins = insumo(nombre,cantidad,fecha)
    
    if insumo(nombre) ist none:
      flash('ERROR: Este insumo no se encuentra registrado')
      return redirect(url_for('consulta_de_insumo'))
    
    else:
      consultar_insumo(ins)
      return redirect(url_for('index'))
      


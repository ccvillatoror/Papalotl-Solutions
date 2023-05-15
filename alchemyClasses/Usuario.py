from alchemyClasses.__init__ import db


class Usuario(db.Model):
    id_usuario = db.Column('idUsuario', db.Integer, primary_key=True) # Entero de autoincremento.
    nombres = db.Column('nombres', db.String(20), nullable=False)
    apellido_p = db.Column('apellidoPaterno', db.String(15), nullable=False)
    apellido_m = db.Column('apellidoMaterno', db.String(15))
    correo = db.Column('correo', db.String(30), nullable=False)
    fecha_nac = db.Column('fechaNacimiento', db.DateTime, nullable=False)
    contrasena = db.Column('contrasena', db.String(25), nullable=False)
    dir_calle = db.Column('calle', db.String(20))
    dir_num = db.Column('numero',db.Integer)
    dir_cp = db.Column('cp', db.String(5))
    dir_colonia = db.Column('colonia', db.String(20))
    dir_ciudad = db.Column('ciudad', db.String(25))
    dir_estado = db.Column('estado', db.String(20))
    tipo_usuario = db.Column('tipoUsuario', db.String(25))

    def __init__(self, nombres, apellido_p, correo, contrasena, fecha_nacimiento, tipo_usuario,
                 apellido_m=None, calle=None, numero=None, cp=None, colonia=None,
                 ciudad=None,estado=None):
        self.nombres = nombres
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_nac= fecha_nacimiento
        self.dir_calle = calle
        self.dir_numero = numero
        self.dir_cp = cp
        self.dir_colonia = colonia
        self.dir_ciudad = ciudad
        self.dir_estado = estado
        self.tipo_usuario = tipo_usuario

    def informacion_envio(self, calle, numero, cp, colonia, ciudad,estado):
        self.dir_calle = calle
        self.dir_numero = numero
        self.dir_cp = cp
        self.dir_colonia = colonia
        self.dir_ciudad = ciudad
        self.dir_estado = estado

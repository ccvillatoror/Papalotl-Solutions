from alchemyClasses.__init__ import db

class usuario(db.Model):

    id_usuario = db.Column('id_usuario', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(200))
    passwd = db.Column('passwd', db.String(40))

    def __init__(self, email, nombre=None, passwd=None):
        self.id_usuario = email
        self.nombre = nombre
        self.passwd = passwd
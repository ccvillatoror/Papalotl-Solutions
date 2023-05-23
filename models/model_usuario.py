from alchemyClasses.Usuario import Usuario
from alchemyClasses.__init__ import db
'''
>>> from yourapp import User
>>> me = User('admin', 'admin@example.com')
>>> db.session.add(me)
>>> db.session.commit()
'''


def obtener_usuario(email_arg):
    ans = Usuario.query.filter(Usuario.correo == email_arg).first()
    return ans

def registrar_usuario(nuevo_usuario):
    db.session.add(nuevo_usuario)
    db.session.commit()
    ans = Usuario.query.filter(Usuario.correo == nuevo_usuario.correo).first()
    return ans



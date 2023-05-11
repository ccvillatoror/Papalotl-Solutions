from alchemyClasses.usuario import usuario
"""
    class Usuario:
        def __init__(self,idUsuario, nombres, apellidoPaterno, apellidoMaterno, correoElectronico, fechaNacimiento, contrasenia, calle, numero, cp, colonia, ciudad, estado,tipoUsuario):
            self.idUsuario=idUsuario 
            self.nombres=nombres 
            self.apellidoPaterno=apellidoPaterno
            self.apellidoMaterno=apellidoMaterno 
            self.correoElectronico=correoElectronico
            self.fechaNacimiento=fechaNacimiento 
            self.contrasenia=contrasenia
            self.calle=calle
            self.numero=numero 
            self.cp=cp 
            self.colonia=colonia 
            self.ciudad=ciudad
            self.estado=estado
            self.tipoUsuario=tipoUsuario

    def __init__(self,nombres, correoElectronico, contrasenia):
        self.nombre=nombres 
        self.correoElectronico=correoElectronico
        self.contrasenia=contrasenia
"""
def obten_usuario(email_arg):
    ans = usuario.query.filter(usuario.id_usuario == email_arg).first()
    return ans
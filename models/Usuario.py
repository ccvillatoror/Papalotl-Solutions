import datetime

class Usuario:
    def __init__(self, idUsuario: int, nombres: str, apellidoP: str, apellidoM: str,
                 correoE: str, contrasena: str, fechaNacimiento: datetime):
        self.idUsuario = idUsuario
        self.nombres = nombres
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.correoE = correoE
        self.contrasena = contrasena
        self.fechaNacimiento = fechaNacimiento
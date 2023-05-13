from Usuario import Usuario
import datetime
class Cliente(Usuario):
    def __init__(self, idUsuario: int, nombres: str, apellidoP: str, apellidoM: str,
                 correoE: str, contrasena: str, fechaNacimiento: datetime,
                 calle: str, numero: int, cp: str, colonia: str, ciudad: str, estado: str):
        super().__init__(idUsuario, nombres, apellidoP, apellidoM, correoE, contrasena, fechaNacimiento)
        self.calle = calle
        self.numero = numero
        self.cp = cp
        self.colonia = colonia
        self.ciudad = ciudad
        self.estado = estado

    def guardarCliente(self):
        return



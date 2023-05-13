class InfoPago:
    def __init__(self, numTarjeta:str, mes, anio, cvv):
        self.numTarjeta = numTarjeta
        self.mes = mes
        self.anio = anio
        self.cvv = cvv
        self.status = False

    def Verificar(self, pasaElPago):
        self.status = pasaElPago
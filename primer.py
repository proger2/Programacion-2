class FernetyCoca:
    fernet = 10
    coca = 5

    def __init__(self,fernet,coca):
        self.fernet = fernet
        self.coca = coca

    def calculo(self):
        if self.fernet < 30 and self.coca > 70:
            print("Ese fernet esta coquiado")


juego = FernetyCoca(20,90)
juego.calculo()


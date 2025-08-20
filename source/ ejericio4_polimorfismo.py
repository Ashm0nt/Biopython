from ejercicio3_herencia import tRNA

"""La clase tRNA ya tiene el metodo de longitud heredado de Gen"""

class Proteina(tRNA):

    def __init__(self, nombre, secuencia_aa, organismo):
        super().__init__(nombre, secuencia="", organismo, anticodon="", aminoacido="")
        self.secuencia_aa = secuencia_aa.upper()

        self.secuencia_aa = secuencia_aa
        


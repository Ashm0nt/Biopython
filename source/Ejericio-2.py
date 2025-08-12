class Gen:
    
    def __init__(self, nombre, secuencia, organismo):
        """Generador y atributos"""
        self.nombre = nombre
        self.organismo = organismo
        self.secuencia = secuencia

    def kilobases(self):
        """Regresa las kilobases del gen"""
        longitud = len(self.secuencia)
        kilobases = longitud / 1000
        return kilobases

    def contenido_gc(self):
        """Calcula el contenido GC de la secuencia"""
        if len(self.secuencia) == 0:
            return 0
        g = self.secuencia.count("G")
        c = self.secuencia.count("C")
        return (g + c) / len(self.secuencia) * 100



gen1 = Gen("AraC", "ATTTATTTGGCGCGCGTAGATTAGA", "E.coli")
print(
    "El gen 1 es:",
    gen1.nombre,
    "Su longitud en kilobases es de:",
    gen1.kilobases(),
    "y tiene un contenido de GC de:",
    round(gen1.contenido_gc(), 2),
    "%"
)

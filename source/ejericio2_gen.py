class Gen:

    def __init__(self, nombre, secuencia, organismo):
        self.nombre = nombre
        self.secuencia = secuencia.upper()
        self.organismo = organismo
    
    def longitud(self):
        return len(self.secuencia)
    
    def porcentaje_gc(self):
        g = self.secuencia.count("G")
        c = self.secuencia.count("C")
        return (g + c) / len(self.secuencia) * 100
    
    def mostrar_info(self):
        return f"Gen: {self.nombre}, Organismo: {self.organismo}, Longitud: {self.longitud()} pb"




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


from source.MontielVargas_AshleyYael_ejercicio2 import Gen


class tRNA(Gen):
    def __init__(self, nombre, secuencia, organismo, anticodon, aminoacido):
        super().__init__(nombre, secuencia, organismo)
        self.anticodon = anticodon.upper().replace("T", "U")  # RNA usa U
        self.aminoacido = aminoacido
        self.carga = False

    def cargar_aminoacido(self):
        self.carga = True
        return f"tRNA {self.nombre} cargado con {self.aminoacido}"
    
    def descargar_aminoacido(self):
        self.carga = False
        return f"tRNA {self.nombre} descargado"
    
    def emparejar_codon(self, codon):
        codon = codon.upper().replace("T", "U")
        if len(codon) != 3:
            return False
        
        pares = {"A":"U", "U":"A", "G":"C", "C":"G"}
        
        for base_codon, base_anticodon in zip(codon, self.anticodon[::-1]): 
            if pares.get(base_codon) != base_anticodon:
                return False
        return True
    
    def participar_traduccion(self, mRNA):
        for i in range(0, len(mRNA)-2, 3):
            if self.emparejar_codon(mRNA[i:i+3]) and self.carga:
                return self.aminoacido
        return None



class ncRNA(Gen):
    def __init__ (self, nombre, organismo, secuencia, tipo, funcion, localizacion):
        Gen.__init__(self, nombre, organismo, secuencia)       
        self.funcion = funcion
        self.tipo = tipo
        self.localizacion = localizacion
        self.proteinas_asociadas = []
        self.dna_asociado = []

    def unirse_a_mRNA(self, mRNA_secuencia):
        if self.secuencia in mRNA_secuencia:
            return f"{self.tipo} {self.nombre} se unió al mRNA"
        return f"{self.tipo} {self.nombre} no se unió al mRNA"

    def unirse_a_proteina(self, proteina):
        if proteina not in self.proteinas_asociadas:
            self.proteinas_asociadas.append(proteina)
        return f"{self.tipo} {self.nombre} se asoció a la proteína {proteina}"

    def interactuar_con_DNA(self, region_DNA):
        if region_DNA not in self.dna_asociado:
            self.dna_asociado.append(region_DNA)
        return f"{self.tipo} {self.nombre} interactuó con la región {region_DNA}"


    
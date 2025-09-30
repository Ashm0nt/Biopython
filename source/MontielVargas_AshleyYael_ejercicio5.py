
from Bio.Seq import Seq

def encontrar_orfs(seq: Seq, min_protein_length=0):
    """
    Encuentra ORFs en las tres tramas de una secuencia de ADN.
    Devuelve una lista de tuplas (frame, start, end, proteína).
    """
    resultado = []

    for frame in range(3):
        traduccion = str(seq[frame:].translate(to_stop=False))
        i = 0
        while i < len(traduccion):
            if traduccion[i] == "M":  # posible inicio
                for j in range(i, len(traduccion)):
                    if traduccion[j] == "*":  # encontrado stop
                        proteina = traduccion[i:j+1]  # incluye el stop
                        if len(proteina) >= min_protein_length:
                            start = frame + i*3 + 1   # coordenada 1-based
                            end = frame + j*3 + 3
                            resultado.append((frame+1, start, end, proteina))
                        i = j
                        break
            i += 1
    return resultado

if __name__ == "__main__":
    dna_seq = Seq(
        "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    )

    # Hebra forward
    orfs_forward = encontrar_orfs(dna_seq)

    # Hebra reverse
    orfs_reverse = encontrar_orfs(dna_seq.reverse_complement())
    orfs_reverse = [("rev"+str(f), s, e, p) for (f, s, e, p) in orfs_reverse]

    # Combinar resultados
    all_orfs = orfs_forward + orfs_reverse

    # Mostrar todos los ORFs
    print("=== ORFs encontrados ===")
    for orf in all_orfs:
        print(orf)

    # ORF más largo
    longest = max(all_orfs, key=lambda x: len(x[-1]))
    print("\n=== ORF más largo ===")
    print(longest)

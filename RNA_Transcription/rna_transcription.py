nucleotide = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'
              }


def to_rna(dna_strand):
    resp = ''
    for i in dna_strand:
        resp += nucleotide[i]
    return resp


print(to_rna('GTA'))
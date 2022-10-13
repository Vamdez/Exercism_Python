
from typing import List
def proteins(strand: str) -> List[str]:
    """Convert from RND sequences into proteins."""
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }
    protein_strand = [codons[strand[i: i + 3]] for i in range(0, len(strand), 3)]
    print(protein_strand)
    return protein_strand[
        : None if "STOP" not in protein_strand else protein_strand.index("STOP")
    ]
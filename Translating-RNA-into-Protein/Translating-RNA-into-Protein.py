codon_table = {}

# https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
with open("Translating-RNA-into-Protein/RNA-codon-table.txt") as f:
    for line in f:
        (codon, amino_acid) = line.rstrip().split(sep=" ")
        codon_table[codon] = amino_acid

with open("Translating-RNA-into-Protein/input.txt") as f:
    rna_str = f.read().rstrip()

# https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length
codons = [rna_str[i: i + 3] for i in range(0, len(rna_str), 3)]

amino_acids = [codon_table[codon] for codon in codons if codon_table[codon] != 'Stop']
print("".join(amino_acids))
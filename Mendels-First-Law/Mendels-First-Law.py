with open('Mendels-First-Law/input.txt') as f:
    for line in f:
        # https://stackoverflow.com/questions/27222079/converting-a-single-line-string-to-integer-array-in-python
        vals = list(map(int, line.split(" ")))

homozygous_dominant = vals[0]
heterozygous = vals[1]
homozygous_recessive = vals[2]
total_individuals = homozygous_dominant + heterozygous + homozygous_recessive
    
p_dominant_1 = (homozygous_dominant / total_individuals)

p_heterozygous_1 = (heterozygous / total_individuals)
p_heterozygous_1_heterozygous_2 = (((heterozygous - 1) / (total_individuals - 1)) * p_heterozygous_1) * 0.75
p_heterozygous_1_dominant_2 = (homozygous_dominant / (total_individuals - 1)) * p_heterozygous_1
p_heterozygous_1_recessive_2 = ((homozygous_recessive / (total_individuals - 1)) * p_heterozygous_1) * 0.5

p_recessive_1 = (homozygous_recessive / total_individuals)
p_recessive_1_dominant_2 = (homozygous_dominant / (total_individuals - 1)) * p_recessive_1
p_recessive_1_heterozygous_2 = ((heterozygous / (total_individuals - 1)) * p_recessive_1) * 0.5

p_dominant = (p_dominant_1 +
    p_heterozygous_1_heterozygous_2 +
    p_heterozygous_1_dominant_2 + 
    p_heterozygous_1_recessive_2 +
    p_recessive_1_dominant_2 +
    p_recessive_1_heterozygous_2)

print(p_dominant)

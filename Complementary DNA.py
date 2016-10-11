__author__ = '116031030'

def generate_complement(strand):
    complement = ''

    for char in strand:
        if char == 'A':
            complement += 'T'

        if char == 'C':
            complement += 'G'

        if char == 'T':
            complement += 'A'

        if char == 'G':
            complement += 'C'

    return complement

dna = input('Input the DNA sequence to generate it\'s complementary: ')

print('The complementary of {} is {}'.format(dna, generate_complement(dna)))

codon = 'UGG'

codon_list = ['UAA', 'UAG', 'UGA']

if codon == 'AUG':
    print('This codon is the start codon.')
# elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
elif codon in codon_list:
    print('This codon is a stop codon.')
else:
    print('This codon is neither a start nor stop codon.')

def Nucleutid_Counter(sequence:str,case_sensetive:bool=False)->dict:
    """
    this function makes a dictionary with keys of each unique charachter of sequence with total number of that charachter repeated in that sequence.
    
    like: 
        Nucleutid_Counter(sequence='ATTTG')
    
    returns:
        {'A':1, 'T':3, 'G':1}
    
    """

    sequence=sequence.upper() if case_sensetive else sequence
    
    counts=dict()
    for nucleotide in sequence:
        counts[nucleotide]=counts.get(nucleotide,0)+1
    return counts

dna_sequence:str=input('dna sequence: ')
print()
print(f'length of dna: {len(dna_sequence)}')
print()

#counting the number of a,t,c,g in the dna sequence


counts=Nucleutid_Counter(sequence=dna_sequence)

# 
# print('A: {}\nC: {}\nG: {}\nT: {}\n'.format(
#     counts['A'],counts['C'],counts['G'],counts['T']))

# rosalind format for output
print('{} {} {} {}'.format(counts['A'],counts['C'],counts['G'],counts['T']))


def Transcribe_DNA_To_RNA(dna_sequence:str)->str:
    """
    Transcribe_DNA_To_RNA is a function designed to convert DNA sequence to RNA sequence with replacing all 'T' with 'U' and returning RNA sequence

    Input parameters:
        dna_sequence -> A string of DNA sequence

    Output:
        rna_sequence -> A string of RNA sequence

    """

    return dna_sequence.upper().replace('T','U')


dna_sequence:str=input('dna sequence: ')

print(Transcribe_DNA_To_RNA(dna_sequence=dna_sequence))
def Create_Strand_Of_DNA(dna_sequence:str,reverse:bool=False)->str:
    """
    
    Create_Strand_Of_DNA designed to create strand DNA sequence which means replace A with T and G with C and reverse
    by setting reverse = True result will reversed
    
    """
    strand_dna={"A":"T","T":"A","G":"C","C":"G"}
    strand_sequence=''.join([strand_dna.get(nucleutid,'') for nucleutid in dna_sequence])
    return strand_sequence if not reverse else strand_sequence[::-1]

rna_to_amino_acid:dict={
    'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'
}

amino_acid_to_rna=dict()
for rna, aa in rna_to_amino_acid.items():# create a dictionary of amino acids to RNA strings that can produce them
    if aa not in amino_acid_to_rna:
        amino_acid_to_rna[aa]=list()
    amino_acid_to_rna[aa].append(rna)

def get_number_of_rna_strings_from_protein(protein:str)->int:
    # Get the number of RNA strings from which the given protein could have been translated, modulo 1,000,000
    number_of_rna_strings:int=len(amino_acid_to_rna['Stop'])# start with the number of RNA strings that can produce the stop codon and they are not in amino acid sequence
    for amino_acid in protein:
        number_of_rna_strings*=len(amino_acid_to_rna[amino_acid])# multiply by the number of RNA strings that can produce the amino acid because of substitutions
        number_of_rna_strings%=1000000
    # Return the number of RNA strings from which the given protein could have been translated, modulo 1,000,000
    return number_of_rna_strings

amino_acid_sequence='MVFQHGWPEWSACPVLCYSIIALENTYMTPDGYRYENSLGYYKCRQTTSKRQKAMPKSDPARNYQNNKWRWVKQGQYKRYHTKWCTSDQCCVGSNVDEARHAIDHFTWQFVIPQPTRYALYLSLMDVTFDYRMAEMQDDGPNNATNTTDSKMSCMGCARYCDRTVFEPHLKLVEVWQATWHPEVLYTLKIGECAMAPDQYWSERASQGYLHHFYLQVYGGEYMWTHCLSVKAHYNIWACSGMNAGNRVMWVSASLRPAMVRNEKVDYKERFVGRLDEDQDYFKSCCVCAEQDACRQSFIRMKMVHTDFFQEIVTDIANAPTNCDIGRIFMITTQAQCSDIHYGTYGQRGTMGVKITTLWTLNDCNREPNGQFPFYHSVANVINIHEVVFFDILTNVDQRVYEPTRPQKMWVMNSHFGPDRFMSEFQNYAFNDWGLIRITEGYGEVAVNKLMLTMRSWSGAFDSQWAPFVWDAIMHWHVCMFYAPDLSNMAPIRGLLFSKNFIRHLIHQHHTGWPQAEAWSLMPPVKFGPQACKQFPTQQGWPALMFVTMLQIHSFQEVSDDQLSVNRMPKNHLWRVCEWAWSDFRLQVGQFTCWHRTINSDADSISIYYDGSHAMQWPIQEVGYKNEAWHKECFCRDTSLIFATHEERSVSQTTNMQFTNNDCHTHVDGDRTRQSDEWLYYYTPWMPAQPARIALKPIIKGKRLKMIQISGPIQFVRDNFVLCCELLWALNYSIKWATVRMLCESGRHSIHDIEISICIDYMEFYFLKIKGVYYQSLWVGAIVYMTREYRGYTLMLLCADTSCCRKIWVDNKWQHRGQIPIPENIGCTEDTQMSMAWWQTNIRRNYARLEQEDEDWVWLMPWNSSVSHIRPYYCAVPPFNQKCSQYMHMTQWDLLDPCHACVMYLNQHSCAIAGYIMQMLYYAEKGIPKKTQILELWIPLGTPKCDVQWINRWVIFLLEWQNLLRDDKEHPGVYSNTINRLKHPYWSYHPCQLMYYTVD'
number_of_posible_rna=get_number_of_rna_strings_from_protein(protein=amino_acid_sequence)

# Output:
print(f'A sequence of amino acid with length:\n\t{len(amino_acid_sequence)}\nmay produced by any of:\n\t{number_of_posible_rna}\nRNA strings posibilities.')
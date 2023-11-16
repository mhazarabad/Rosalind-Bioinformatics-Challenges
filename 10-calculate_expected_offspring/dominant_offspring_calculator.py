def Dominant_Offspring_Calculator(
        number_of_AA_AA:int, number_of_AA_Aa:int, number_of_AA_aa:int, 
        number_of_Aa_Aa:int, number_of_Aa_aa:int, number_of_aa_aa:int
    )->float:
    """
    
    this function calculates the expected number of offspring displaying the dominant phenotype
    given the number of couples with the following genotypes:
        AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

    probability of dominant offspring from each genotype:
        AA-AA: 1.0
        AA-Aa: 1.0
        AA-aa: 1.0
        Aa-Aa: 0.75
        Aa-aa: 0.5
        aa-aa: 0.0

    ### but it returns float because it is the expected number of offspring which is statistically calculated
    
    """
    
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_AA_PARENT = 1.0
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_Aa_PARENT = 1.0
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_aa_PARENT = 1.0
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_Aa_Aa_PARENT = 0.75
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_Aa_aa_PARENT = 0.5
    PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_aa_aa_PARENT = 0.0

    number_of_offspring = 2 # which means each couple has exactly 2 children

    return ((
        number_of_AA_AA * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_AA_PARENT + # number of offspring with dominant phenotype from AA-AA
        number_of_AA_Aa * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_Aa_PARENT + # number of offspring with dominant phenotype from AA_Aa
        number_of_AA_aa * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_AA_aa_PARENT + # number of offspring with dominant phenotype from AA_aa 
        number_of_Aa_Aa * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_Aa_Aa_PARENT + # number of offspring with dominant phenotype from Aa_Aa
        number_of_Aa_aa * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_Aa_aa_PARENT + # number of offspring with dominant phenotype from Aa_aa
        number_of_aa_aa * PROBABILITY_OF_DOMINANT_OFFSPRING_FROM_aa_aa_PARENT   # number of offspring with dominant phenotype from aa_aa
    )*number_of_offspring) # multiply by the number of offspring per couple

print(Dominant_Offspring_Calculator(1, 0, 0, 1, 0, 1))# should be 3.5


PROBABILITY_RECESSIVE_PHENOTYPE_IF_BOTH_HETO=1/4
"""
   Y  y
Y  YY Yy
y  Yy yy

"""
PROBABILITY_RECESSIVE_PHENOTYPE_IF_ONE_HETRO_ONE_DOMINANT=0
"""
   Y  y
Y  YY Yy
Y  YY Yy

"""
PROBABILITY_RECESSIVE_PHENOTYPE_IF_ONE_HETRO_ONE_RECESSIVE=1/2
"""
   Y  y
y  Yy yy
y  Yy yy

"""
PROBABILITY_RECESSIVE_PHENOTYPE_IF_BOTH_DOMINANT=0
"""
   Y  Y
Y  YY YY
Y  YY YY

"""
PROBABILITY_RECESSIVE_PHENOTYPE_IF_BOTH_RECESSIVE=1
"""
   y  y
y  yy yy
y  yy yy

"""

def Probability_Of_Recessive_Phenotype(homozygous_dominant:int,heterozygous:int,homozygous_recessive:int)->float:
   result=[]
   pop_first_choice=homozygous_dominant+heterozygous+homozygous_recessive
   pop_second_choice=homozygous_dominant+heterozygous+homozygous_recessive-1

   both_hetro=(heterozygous/pop_first_choice)*((heterozygous-1)/pop_second_choice)
   result.append((both_hetro*PROBABILITY_RECESSIVE_PHENOTYPE_IF_BOTH_HETO))

   one_hetro_one_recessive=(heterozygous/pop_first_choice)*(homozygous_recessive/pop_second_choice)
   one_recessive_one_hetro=(homozygous_recessive/pop_first_choice)*(heterozygous/pop_second_choice)
   result.append(((one_hetro_one_recessive+one_recessive_one_hetro)*PROBABILITY_RECESSIVE_PHENOTYPE_IF_ONE_HETRO_ONE_RECESSIVE))

   both_homo_recessive=(homozygous_recessive/pop_first_choice)*((homozygous_recessive-1)/pop_second_choice)
   result.append((both_homo_recessive*PROBABILITY_RECESSIVE_PHENOTYPE_IF_BOTH_RECESSIVE))

   return sum(result)

def Probability_Of_Domaninat_Phenotype(homozygous_dominant:int,heterozygous:int,homozygous_recessive:int)->float:
   return 1-Probability_Of_Recessive_Phenotype(homozygous_dominant,heterozygous,homozygous_recessive)


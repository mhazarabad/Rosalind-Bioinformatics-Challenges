def Hamming_Distance_Calculator(seq_1:str,seq_2:str)->int:
    base_distance=len(seq_1)-len(seq_2) if len(seq_1)>len(seq_2) else len(seq_2)-len(seq_1)
    return sum(s1!=s2 for s1,s2 in zip(seq_1,seq_2))+base_distance

print(Hamming_Distance_Calculator(
    seq_1='',
    seq_2='',
))
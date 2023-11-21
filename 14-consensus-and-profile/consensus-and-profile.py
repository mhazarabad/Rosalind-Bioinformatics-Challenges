def Read_Genomes(file_path: str) -> dict:
    result=dict()
    with open(file_path,'r') as file:
        for line in file.readlines():
            if line.startswith('>'):
                genome_name=line[1:].strip()
                result[genome_name]=''
            else:
                result[genome_name]+=line.strip()
    return result
        
def Genome_Profile_Calculator(genomes: dict) -> dict:
    whole_genome_length=len(list(genomes.values())[0])
    result={
        "A":[0]*whole_genome_length,
        "C":[0]*whole_genome_length,
        "G":[0]*whole_genome_length,
        "T":[0]*whole_genome_length
    }
    nucleotide_index=0
    while nucleotide_index<whole_genome_length:
        for genome in genomes.values():
            result[genome[nucleotide_index]][nucleotide_index]+=1
        nucleotide_index+=1
    return result

def Consensus_Sequencer(profiles: dict) -> str:
    result=''
    for i in range(len(list(profiles.values())[0])):
        max_value=0
        max_nucleotide=''
        for nucleotide,count in profiles.items():
            if count[i]>max_value:
                max_value=count[i]
                max_nucleotide=nucleotide
        result+=max_nucleotide
    return result

profiles=Genome_Profile_Calculator(Read_Genomes('14-consensus-and-profile/input_file.fasta'))

print(Consensus_Sequencer(profiles))
for nucleutid,profile in profiles.items():
    print(nucleutid+': '+' '.join(map(str,profile)))
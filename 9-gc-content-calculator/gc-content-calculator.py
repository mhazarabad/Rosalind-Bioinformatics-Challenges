
def Read_FastA(file_fasta_path:str)->list:
    records=[]
    with open(file_fasta_path,'r') as file_fasta:
        record=[]
        name=''
        sequence=''
        for line in file_fasta:
            if line[0]=='>':
                
                if sequence:
                    record.append(name)
                    name=''
                    record.append(sequence)
                    sequence=''
                    records.append(record)
                    record=[]
                    sequence=''
                name=line[1:].strip()
            else:
                sequence+=line.strip()
        record.append(name)
        record.append(sequence)
        records.append(record)
                
    return records

def GC_Contet_Calculator(sequence:str)->float:
    return (sequence.count('G')+sequence.count('C'))/len(sequence)

def Records_GC_Content_Calculator(records:list)->list:
    return [{'name':record[0],'sequence':record[1],'gc-content':GC_Contet_Calculator(record[1])} for record in records]

def Get_Highest_GC_Content_Record(records:list)->dict:
    return max(records,key=lambda record:record['gc-content'])

file_fasta_path='9-gc-content-calculator/gc.fasta'

records=Read_FastA(file_fasta_path)
gc_calculated_records=Records_GC_Content_Calculator(records)
highest_gc=Get_Highest_GC_Content_Record(gc_calculated_records)
print(highest_gc['name'])
print(f'{highest_gc["gc-content"]*100:.6f}')

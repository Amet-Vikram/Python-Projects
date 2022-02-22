
nucleotides = ["A", "T", "G", "C"]


seq = 'AAAACCCGGT'  
def validateSeq(dna_seq):
    temp_seq = dna_seq.upper()
    for i in temp_seq:

        if i not in nucleotides:
            return False
    return temp_seq

def countNuc(dna_seq):
    nuc_count = 0
    for nuc in dna_seq:
        nuc_count += 1
    return nuc_count

def countNucFreq(dna_seq):
    tempFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in dna_seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict

def transcript(dna_seq):
    return dna_seq.replace('T', 'U')

def revComplement(dna_seq):
    com1 = dna_seq.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T')
    com2 = com1.replace('G', '%temp%').replace('C', 'G').replace('%temp%', 'C')
    return com2[::-1]


def wordCount(string):
    
    dictionary = {}
    words = string.split()
    
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        
        else:
            dictionary[word] = 1
    for key, values in dictionary.items():
        print(key, values)


def rabbitPairs(months, offsprings):
    parent, child = 1, 1
    for i in range(months - 1):
        child, parent = parent , parent + (child * offsprings)
    return child




'''def codonSplit(dna_seq):
    codonlist = []
    if len(dna_seq)%3 ==0:  
        for i in range(0, len(dna_seq), 3):
            codon = dna_seq[i: i + 3]
            codonlist.append(codon)
    return codonlist

    elif len(dna_seq)%3 !=0:
        print('Missing Nucleotides')
'''
        

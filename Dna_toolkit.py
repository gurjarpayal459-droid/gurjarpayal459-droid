#Biotech DNA analysis toolkit
#Author:payal gurjar - btech biotechnology,1st year ,IIMT University-Meerut
#Description: Python tool that takes a DNA sequence and give you GC%
#RNA Transcript component, complement, reverse complement+ biological interpretation
#Built for biotech students to learn bioinformatics basics
def dna_analysis_toolkit(dna_sequence):  
    """
    Analyzes a DNA sequence and returns key biological metrics.
    This is the foundation for future Bio-AI projects.
    """
    #Clean and Standardize the input sequence
    dna = dna_sequence.upper().strip()
    #validation : Check if sequence contain only A,T,G,C .
    if not all(base in 'ATGC' for base in dna):
        print("Error! Invalid DNA sequence. Only A,T,G,C are allowed")
        return   
    
    # Feature 1: Basic Sequence Information
    sequence_length = len(dna)
    count_a = dna.count('A')
    count_t = dna.count('T')
    count_g = dna.count('G')
    count_c = dna.count('C')
    
    # Feature 2: GC Content - BioTech ka sabse important
    gc_count = count_g + count_c
    gc_content = (gc_count / sequence_length) * 100
    
    # Print Results
    print("--- DNA Analysis Report ---")
    print(f"Sequence Length: {sequence_length} bp")
    print(f"A: {count_a}, T: {count_t}, G: {count_g}, C: {count_c}")
    print(f"GC Content: {gc_content:.2f}%")
    # Feature 3: RNA + Complement
    rna = dna.replace('T', 'U')
    complement = dna.translate(str.maketrans('ATGC', 'TACG'))
    rev_complement = complement[::-1]
    
    print(f"RNA Transcript: {rna}")
    print(f"Complement: {complement}")
    print(f"Reverse Complement: {rev_complement}")
# Test the function
dna_analysis_toolkit("ATGTATGC")  
  
   

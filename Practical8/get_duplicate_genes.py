import re

def read_fasta(input_file, output_file=None):
    sequences = {}  
    current_sequence_name = None  
    current_sequence = ''  

    with open(input_file, 'r') as fasta_file:  
        for line in fasta_file:  
            line = line.strip() 
            if line.startswith('>'):  
                if current_sequence_name:  
                    sequences[current_sequence_name] = current_sequence  
                    
                    if output_file:
                        with open(output_file, 'a') as out_f:
                            out_f.write(current_sequence_name + '\n')
                            out_f.write(current_sequence + '\n')
                current_sequence_name = line[1:]  
                current_sequence = ''  
            else:  
                current_sequence += line  

        
        if current_sequence_name:  
            sequences[current_sequence_name] = current_sequence  
            
            if output_file:
                with open(output_file, 'a') as out_f:
                    out_f.write(current_sequence_name + '\n')
                    out_f.write(current_sequence + '\n')

    return sequences  


input_fasta_file = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'  
output_fasta_file = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical8/duplicate_genes.fa'  
sequences = read_fasta(input_fasta_file, output_fasta_file)  




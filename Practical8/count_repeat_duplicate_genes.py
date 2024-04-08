import re
import os

def read_fasta(file_path):
    sequences = {}  
    current_sequence_name = None  
    current_sequence = ''  

    with open(file_path, 'r') as fasta_file:  
        for line in fasta_file:  
            line = line.strip()  
            if line.startswith('>'):  
                if current_sequence_name:  
                    sequences[current_sequence_name] = current_sequence  
                current_sequence_name = line[1:]  
                current_sequence = ''  
            else:  
                current_sequence += line 

        
        if current_sequence_name:  
            sequences[current_sequence_name] = current_sequence  

    return sequences  

def count_repeats(seq, repeat_pattern):
    return len(re.findall(repeat_pattern, seq))

def write_fasta(output_file, sequences):
    with open(output_file, 'w') as out_f:
        for gene_name, sequence in sequences.items():
            repeat_count = count_repeats(sequence, repeat_pattern)
            out_f.write(f'>{gene_name}_{repeat_count}\n{sequence}\n')


input_fasta_file = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'


repeat_sequence = input("请输入一个重复序列（GTGTGT或GTCTGT）: ")
repeat_pattern = repeat_sequence


output_directory = '/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical8/'
output_file_name = os.path.join(output_directory, f"{repeat_sequence}_duplicate_genes.fa")


sequences = read_fasta(input_fasta_file)
filtered_sequences = {gene_name: sequence for gene_name, sequence in sequences.items() if repeat_sequence in sequence}


write_fasta(output_file_name, filtered_sequences)

print(f"包含重复序列'{repeat_sequence}'的基因已写入到文件'{output_file_name}'中。")

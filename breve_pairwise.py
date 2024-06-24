def read_fasta(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        sequence = ''.join(lines[1:]).replace('\n', '')
    return sequence

def compare_sequences(seq1, seq2):
    differences = 0

    if len(seq1) != len(seq2):
        print ("Sequences are not of the same length.")
    
    for a, b in zip(seq1, seq2):
        if a != b:
            differences = differences + 1

    return differences

file1 = "/home/ubuntu/wdir/PopGenStats_Project/output_breve_genomes/SQK-NBD114-96_barcode01.fna"
file2 = "/home/ubuntu/wdir/PopGenStats_Project/output_breve_genomes/SQK-NBD114-96_barcode02.fna"

seq1 = read_fasta(file1)
seq2 = read_fasta(file2)
    
differences = compare_sequences(seq1, seq2)

print(f"Number of differing positions: {differences}")

import glob
import os

def read_fasta(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        sequence = ''.join(lines).replace('\n', '')
    return sequence

def compare_sequences(seq1, seq2):
    differences = 0

    if len(seq1) != len(seq2):
        print ("Sequences are not of the same length.")
        # Need to make this print file names as well
    
    for a, b in zip(seq1, seq2):
        if a != b:
            differences += 1

    return differences

fnames = glob.glob('/home/ubuntu/wdir/PopGenStats_Project/output_breve_genomes/SQK-NBD114-96*.fna')
sequences = {}

for f in fnames:
    sequences[f] = read_fasta(f)

for i, file1 in enumerate(fnames):
    for file2 in fnames[i+1:]:
        seq1 = sequences[file1]
        seq2 = sequences[file2]
        differences = compare_sequences(seq1, seq2)

        print(f"Differences between {os.path.basename(file1)} and {os.path.basename(file2)}: {differences}")

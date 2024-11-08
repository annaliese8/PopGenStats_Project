import glob
import os
import numpy
import seaborn as sns
import matplotlib.pyplot as plt 

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

fnames = glob.glob('/home/ubuntu/wdir/PopGenStats_Project/output_infantis_genomes/infantis_genomes/*')
sequences = {}

num_files = len(fnames)
difference_matrix = numpy.zeros((num_files, num_files))

for f in fnames:
    sequences[f] = read_fasta(f)

fnames.sort()

for i, file1 in enumerate(fnames):
    for j, file2 in enumerate(fnames):
        if i != j:
            seq1 = sequences[file1]
            seq2 = sequences[file2]
            differences = compare_sequences(seq1, seq2)
            #print(f"Differences between {os.path.basename(file1)} and {os.path.basename(file2)}: {differences}")

            divergence = (differences/len(seq1)) * 100

            print (max(divergence))

            if divergence >=1:
                print(f"% divergence between {file1} and {file2} = {divergence}")
# calculate max

            difference_matrix[i, j] = differences

#print(f"Difference Matrix: {difference_matrix}")

# map = sns.clustermap(difference_matrix)
# plt.show()

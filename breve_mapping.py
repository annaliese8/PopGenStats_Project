import gzip
import glob
import os

def read_reference(fname):
    reference = {}
    with gzip.open(fname, 'rb') as f:
        for line in f:
            line = line.decode('utf-8').strip()

            # split each character into a list item, select the first one, remove the '>' character
            if line.startswith('>'):
                header = line.split()[0][1:]
                reference[header] = []
                continue

            # Puts list back together; overall goes from '>ABCDE' (FASTA format) to 'ABCDE'
            reference[header].append(line)

    for header, sequences in reference.items():
        # concatenation (new list, appends like a zipper (with '' in between each sequence))
        reference[header] = list(''.join(sequences))
        # Print contigs
        print (header, len(reference[header]))

    return reference

def read_vcf(fnames):
    with open(fnames) as f:
        for line in f:
            if line.startswith('##'):
                continue

            if line.startswith('#'):
                # Split header row by column
                header = line.strip().split('\t')
                continue

            # strip to remove whitespace (tabs), split by tabs
            line = line.strip().split('\t')
            # implement into dictionary - each line in vcf gets a dict
            line = dict(zip(header, line))

            print (line)

            break

fname = '/Users/Annaliese/Desktop/GIS_Practice_Project/data/BifidoIsolates/breve/GCA_024665435.1_ASM2466543v1_genomic.fna.gz'
ref = read_reference(fname)

fnames = '/Users/Annaliese/Desktop/GIS_Practice_Project/data/BifidoIsolates/breve/breve.vcalling.longshot.vcf.tar/minimap2/breve/*.longshot.vcf'
fnames = glob.glob(fnames)

for fname in fnames:
    sample = os.path.basename(fname)
    sample = sample[:-13]
    print (sample)
    read_vcf(fname)    

# In this example, we have 2 contigs: CP102536.1  2330951
#                                     CP102537.1  5749
# We can get more than one contig if the reference read is off (unlikely), or if plasmids are present
# In this case, the second contig is most likely a plasmid because it is so much smaller

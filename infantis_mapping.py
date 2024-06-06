import gzip
import glob
import os

def read_reference(fname):
    reference = {}
    with gzip.open(fname, 'rb') as f:
        for line in f:
            line = line.decode('utf-8').strip()

            if line.startswith('>'):
                header = line.split()[0][1:]
                reference[header] = []
                continue

            reference[header].append(line)

    for header, sequences in reference.items():
        reference[header] = list(''.join(sequences))
        print (header, len(reference[header]))

    return reference

def read_vcf(fnames):
    with open(fnames) as f:
        for line in f:
            if line.startswith('##'):
                continue

            if line.startswith('#'):
                header = line.strip().split('\t')
                continue

            line = line.strip().split('\t')
            line = dict(zip(header, line))

            print (line)

            break

fname = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/infantis/GCA_900637215.1_49888_B01_genomic.fna.gz'
ref = read_reference(fname)

# infer SNP from each sample into reference genome (so we have a complete genome of each file)

fnames = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/infantis/infantis.vcalling.longshot.vcf.tar/minimap2/infantis/*.longshot.vcf'
fnames = glob.glob(fnames)

for fname in fnames:
    sample = os.path.basename(fname)
    sample = sample[:-13]
    print (sample)
    read_vcf(fname)    

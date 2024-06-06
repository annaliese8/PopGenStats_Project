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
        # # Print contigs
        # print (header, len(reference[header]))

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

def insert_snps(reference, vcf_data, output_file):
    updated_reference = reference
    # sample_genome = output_file

    for snp in vcf_data:
        chrom = snp['#CHROM']
        pos = int(snp['POS']) - 1 # turn into an int and make it 0-based
        ref = snp['REF']
        alt = snp['ALT']

        if updated_reference[chrom][pos] == ref:
            updated_reference[chrom][pos] = alt
        else:
            print("Ref base at {chrom}:{pos+1} does not match reference genome")

        return updated_reference
    
def write_sample_genome(updated_reference, sample_name, output_file):
    for header, sequence in updated_reference.items():
            with open(os.path.join(output_file, "{sample_name}.fna")) as f:
                f.write(">{header}\n")
                #WIP

fname = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/breve/GCA_024665435.1_ASM2466543v1_genomic.fna.gz'
fnames = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/breve/breve.vcalling.longshot.vcf.tar/minimap2/breve/*.longshot.vcf'
output_file = '/Users/Annaliese/Desktop/PopGenStats_Project/output_genomes'
os.makedirs(output_file, exist_ok=True)

ref = read_reference(fname)
fnames = glob.glob(fnames)

for vcf in fnames:
    vcf_data = read_vcf(vcf)
    sample_name = os.path.basename(vcf).replace('.longshot.vcf', '')
    updated_reference = insert_snps(ref, vcf_data)
    write_sample_genome(updated_reference, sample_name, output_file)
    print ('{sample_name} completed!')

# for fname in fnames:
#     sample = os.path.basename(fname)
#     sample = sample[:-13]
#     print (sample)
#     read_vcf(fname)    

# In this example, we have 2 contigs: CP102536.1  2330951
#                                     CP102537.1  5749
# We can get more than one contig if the reference read is off (unlikely), or if plasmids are present
# In this case, the second contig is most likely a plasmid because it is so much smaller

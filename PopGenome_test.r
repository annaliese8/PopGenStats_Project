library(PopGenome)

GENOME.class <- readData("/home/ubuntu/wdir/PopGenStats_Project/output_infantis_genomes/infantis_genomes/")
GENOME.class <- diversity.stats(GENOME.class)

#show the result:
GENOME.class@nuc.diversity.within

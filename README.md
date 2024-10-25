Our lab has Nanopore sequencing data for Bifidobacterium longum and Bifidobacterium breve isolates taken from Singaporean stool samples. As such, we are interested in finding a method to robustly cluster microbial samples at the strain-level. At the species-level, genetic clustering is more defined due to clearer disjunctions in sample genomes. However, due to the high genetic similarity between samples within a species, this aim is not as simple as decreasing the scale of species-level clustering. If we attempt to do this, the samples will either all get clustered together or form clusters that are not robust due to the continuum of genetic differentiation across the samples.

To do this, we implemented agglomerative hierarchical clustering methods on four sets of same-species samples. Two of these species data contained isolate data obtained from our lab. On these two species we also performed dereplication methods to explore alternative clustering methods.

For pipeline analysis, use `strain_level_clustering.ipynb` and input species name in the format "G_species"

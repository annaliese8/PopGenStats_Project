import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, ward
from scipy.spatial.distance import pdist

# file_path = '/home/ubuntu/wdir/PopGenStats_Project/data/BifidoIsolates/BLongum/mummer.tsv.gz'
file_path = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/BLongum/mummer.tsv'

columns_to_use = ['prc_aligned1', 's1', 's2']
chunk_list = []

#for chunk in pd.read_csv(file_path, sep = '\t', usecols = columns_to_use, chunksize = 10000):
#    chunk_list.append(chunk)

#mummer_matrix = pd.concat(chunk_list)

mummer_matrix = pd.read_csv(file_path, sep='\t', index_col=0)

mummer_matrix['score1'] = mummer_matrix['avg_identity1'] * (mummer_matrix['prc_aligned1'] / 100)
mummer_matrix['score2'] = mummer_matrix['avg_identity2'] * (mummer_matrix['prc_aligned2'] / 100)

print (mummer_matrix)

upper_triangle = mummer_matrix.pivot(index='s1', columns='s2', values='score1').fillna(0)
lower_triangle = mummer_matrix.pivot(index='s2', columns='s1', values='score2').fillna(0)
mummer_matrix = upper_triangle + lower_triangle
mummer_matrix[:] = np.where(mummer_matrix==0, 100, mummer_matrix)
# mummer_matrix.replace([np.inf, -np.inf], 0)

print (upper_triangle)
print(mummer_matrix.describe())
exit(1)

sns.clustermap(mummer_matrix, row_cluster=False, col_cluster=False)
plt.show()

print(mummer_matrix)
exit(1)

distance_matrix = pdist(mummer_matrix)
linkage_matrix = ward(distance_matrix)
print(linkage_matrix)
exit(1)

dendrogram(linkage_matrix)
plt.show()

# sns.clustermap(mummer_matrix, row_cluster=False, col_cluster=False)
# #sns.clustermap(mummer_matrix)
# plt.show()

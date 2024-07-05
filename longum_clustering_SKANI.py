import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# file_path = '/home/ubuntu/wdir/PopGenStats_Project/data/BifidoIsolates/BLongum/skani_ani_edge_list.tsv.gz'
file_path = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/BLongum/skani_ani_edge_list.tsv'

columns_to_use = ['Ref_file', 'Query_file', 'ANI']
chunk_list = []

for chunk in pd.read_csv(file_path, sep = '\t', usecols = columns_to_use, chunksize = 10000):
    chunk_list.append(chunk)

# chunk_list.sort()

skani_matrix = pd.concat(chunk_list)

skani_pivot = skani_matrix.pivot(index = 'Ref_file', columns = 'Query_file', values = 'ANI')
skani_pivot = skani_pivot.fillna(0)

sns.clustermap(skani_pivot)
plt.show()

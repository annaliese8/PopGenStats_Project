import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# file_path = '/home/ubuntu/wdir/PopGenStats_Project/data/BifidoIsolates/BLongum/mummer.tsv.gz'
file_path = '/Users/Annaliese/Desktop/PopGenStats_Project/data/BifidoIsolates/BLongum/mummer.tsv.gz'

columns_to_use = ['prc_aligned1', 's1', 's2']
chunk_list = []

for chunk in pd.read_csv(file_path, sep = '\t', usecols = columns_to_use, chunksize = 10000):
    chunk_list.append(chunk)

skani_matrix = pd.concat(chunk_list)

skani_pivot = skani_matrix.pivot(index = 's1', columns = 's2', values = 'prc_aligned1')
skani_pivot = skani_pivot.fillna(0)

sns.clustermap(skani_pivot)
plt.show()

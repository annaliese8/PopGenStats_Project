import seaborn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = '/home/ubuntu/wdir/PopGenStats_Project/data/BifidoIsolates/BLongum/skani_ani_edge_list.tsv'
skani_matrix = pd.read_csv(file_path, sep='\t')

# pivot_table = skani_matrix.pivot_table(
#     index='Ref_name',
#     columns='Query_name',
#     values='ANI'
# )
# pivot_table = pivot_table.fillna(0)

skani_matrix = np.array(skani_matrix)[:,[2,3,4]]

# print("The Kth column of matrix is : " + str(res))

seaborn.clustermap(skani_matrix)
plt.show()

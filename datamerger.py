import pandas as pd
import glob

path_data = '../data/'

files = glob.glob(path_data + 'processed/' + '*.csv')

df_genes = pd.read_excel(path_data + 'genes.xlsx')

df_collection = pd.DataFrame() # Initialize df to add data later
for i in files:
    df = pd.read_csv(i, index_col=False)

    # Get entrezID
    entrezID = df.iloc[0]['ID']
    #print(entrezID)

    HGNC = df_genes.loc[df_genes['entrezID'] == entrezID]
    HGNC = HGNC.iloc[0]['HGNC']
    print(HGNC)

    df['Gene Symbol'] = HGNC
    df = df.drop('Feature', axis=1)

    df_collection = df_collection.append(df, ignore_index=True)

#print(df_collection)

gene_shRNA = df_collection['Gene Symbol'] + '.' + df_collection['shRNA.name'].str.split('_', 2, expand=True)[2]
df_collection['gene_shRNA'] = gene_shRNA

df_collection.to_excel(path_data + '97mer.xlsx', index=False)

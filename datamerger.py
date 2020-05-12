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

df_collection.to_excel(path_data + '97mer.xlsx', index=False)


    ## Get list of 97mers, 5 in total
    #list_97mer = df['97mer.construct'].tolist()
    #df_collection[entrezID] = list_97mer


#df_collection = df_collection.T # Transpose table
#
## Get list of gene names and set entrezID as index for join
#
#df_collection = df_collection.join(df_genes, how='inner')
#
## Reorder columns
#df_collection = df_collection[['HGNC', 0, 1, 2, 3, 4]]
#print(df_collection)
#

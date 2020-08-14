Folder structure:\
+-- data\
|   +-- processed\
|   +-- raw\
+-- script\

1. Convert HGNC symbols to entrezID and save to data/genes.xlsx\
https://www.ensembl.org/biomart/martview
- Ensembl Genes 100
- Human genes (GRCh38.p13)
- Filter/Gene/Input external references ID list: HGNC symbol(s) [e.b.A1BG]\
- Attributes/External References: HGNC symbol, NCBI gene (formerly Entrezgene) ID\
- Download results as "genes.csv"
2. Rename columns to "entrezID" and "HGNC"
3. Check for missing entries in "entrezID" and replace manually
4. webscraper.py: Downloads csv file from splashRNA\
5. Copy files from "data/raw" to "data/processed"\
6. truncate3lines: bash script to remove first 3 lines from all csv files in "data/processed"\
7. datamerger.py: Compile individual csv files into single file. Creates "data/97mer.xlsx"

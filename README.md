Folder structure:\
+-- data\
|   +-- processed\
|   +-- raw\
+-- script\

1. Convert HGNC symbols to entrezID and save to data/genes.xlsx\
https://www.ensembl.org/biomart/martview
	1. Ensembl Genes 100
	2. Human genes (GRCh38.p13)
	3. Filter/Gene/Input external references ID list: HGNC symbol(s) [e.b.A1BG]
	4. Attributes/External References: HGNC symbol, NCBI gene (formerly Entrezgene) ID
	5. Download results as "genes.xlsx"
2. Rename columns to "entrezID" and "HGNC"
3. Check for missing entries in "entrezID" and replace manually
4. webscraper.py: Downloads csv file from splashRNA\
5. Copy files from "data/raw" to "data/processed"\
6. truncate3lines: bash script to remove first 3 lines from all csv files in "data/processed"\
7. datamerger.py: Compile individual csv files into single file. Creates "data/97mer.xlsx"

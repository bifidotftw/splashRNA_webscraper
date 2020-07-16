Folder structure:\
+-- data\
|   +-- processed\
|   +-- raw\
+-- script\

1. Convert HGNC symbols to entrezID and save to data/genes.xlsx\
https://www.ensembl.org/biomart/martview\
- Filter: specify list of HGNC symbols\
- Attributes: Convert "HGNC symbol" to "NCBI gene (formerly Entrezgene) ID"\
2. webscraper.py: Downloads csv file from splashRNA\
3. Copy files from "data/raw" to "data/processed"\
4. truncate3lines: bash script to remove first 3 lines from all csv files in "data/processed"\
5. datamerger.py: Compile individual csv files into single file. Creates "data/97mer.xlsx"

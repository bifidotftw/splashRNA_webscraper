from mechanize import Browser
import pandas as pd
import csv
import time

path_data = '../data/'


br = Browser()


df = pd.read_excel(path_data + 'genes.xlsx')
list_entrezID = df['entrezID'].tolist()

for entrezID in list_entrezID:
    site = br.open('http://splashrna.mskcc.org/')

    '''
    Site only contains 1 form which contains all the input fields
    Form is unnamed -> selected by position 0
    '''
    br.select_form(nr=0)

    br.form['fasta'] = '> entrezID\r\n' + str(entrezID)
    br.form['academic'] = ['on']
    br.form['email'] = 'p.biechl@dkfz.de'

    response = br.submit()

    br.select_form(nr=1) # In response page the second form contains the information

    br.form.action='http://splashrna.mskcc.org/splashRNA_results.csv' #Performs the action that would be called when the download button is clicked
    result = br.submit() # Submit request

    # Result is a binary file that contains the data as csv
    data = result.read()
    data = data.decode() # Convert binary file to files

    # Save file as csv
    with open(path_data + 'raw/' + str(entrezID) + '.csv', 'w') as f:
        f.write(data)

    print(str(entrezID) + ' done')
    time.sleep(10) # Wait 10s to relieve server

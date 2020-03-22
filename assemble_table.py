from itertools import cycle
import glob
from collections import defaultdict
from copy import deepcopy

def load_from_csv(path_name, sep='\t'):
    
    data = open(path_name, 'rt').read()
    data = data.strip('\n')
    data = data.split('\n')
    headers = ['sample', 'hit_id', 'hit_name', 'evalue', 'bitscore', 'score', 'pident'] #hardcoded because blastn output does not add headers to the tabular data file
    
    table = list()
    headers_cycle = cycle(headers)
    count = set() #for counting unique samples
    
    for row in data:
        row = row.split(sep)
        data_dict = dict()
        for element in row:
            data_dict[headers_cycle.__next__()] = element
        if table != [] and data_dict['sample'] == table[-1]['sample'] and data_dict['bitscore'] != table[-1]['bitscore']:
            pass #since the blastn output is already sorted, I'm appending only the blast hits that have the highest bitscore (it's important to note some sequences yielded multiple same score hits, those are being added as multiple hits here)
        else:
            table.append(data_dict)
        count.add(data_dict['sample'])
    
    print(path_name)
    print('Number of unique samples: ', len(count), '\n')

    return headers, table

def write_to_csv(headers, data, path_name, sep='\t'):
    
    result = [sep.join(headers)]
    
    for row in data:
        ordered_row = list()
        for element in headers:
            try:
                ordered_row.append(str(row[element]))
            except(KeyError):
                ordered_row.append('0') #missing data returns '0'
        result.append(sep.join(ordered_row))
    
    result = '\n'.join(result)
    
    open(path_name, 'w').write(result)

###

new_table = list()
species = set()
new_table_headers = ['date']

for filename in sorted(glob.iglob('blastn_results/*.csv'), key=lambda x: int(x[18:-21])):
    print(filename)

    day = defaultdict(int)
	
    head, table = load_from_csv(filename)

    for row in table:
        species.add(row['hit_name'])
        day[row['hit_name']] += 1 #each dwp gets a dict of species and how many hits for that species
	
    new_table.append({**{'date': filename[15:-21]}, **deepcopy(day)})

new_table_headers += sorted(list(species))
write_to_csv(new_table_headers, new_table, 'blastn_results_matrix.csv')

###
#transposing of csv
#credit: https://stackoverflow.com/questions/4869189/how-to-transpose-a-dataset-in-a-csv-file
from csv import reader, writer 
with open('blastn_results_matrix.csv') as f, open('blastn_results_matrix_t.csv', 'w') as fw: 
    writer(fw, delimiter='\t').writerows(zip(*reader(f, delimiter='\t')))

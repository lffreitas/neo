from itertools import cycle
from collections import defaultdict

def load_from_csv(path_name, sep='\t'):
    
    data = open(path_name, 'rt').read()
    data = data.strip('\n')
    data = data.split('\n')
    headers = data.pop(0).split(sep)
    
    table = list()
    headers_cycle = cycle(headers)
    
    for row in data:
        row = row.split(sep)
        data_dict = dict()
        for element in row:
            data_dict[headers_cycle.__next__()] = element
        table.append(data_dict)
    
    return headers, table

def write_to_csv(headers, data, path_name, sep='\t'):
    
    result = [sep.join(headers)]
    
    for row in data:
        ordered_row = list()
        for element in headers:
            try:
                ordered_row.append(str(row[element]))
            except(KeyError):
                ordered_row.append('0')
        result.append(sep.join(ordered_row))
    
    result = '\n'.join(result)
    
    open(path_name, 'w').write(result)


head, table = load_from_csv('blastn_results_matrix.csv')

all_species = defaultdict(int)

for line in table:
    for sp in head[1:]:
        all_species[sp] += int(line[sp])

new_head = [head[0]]

new_head += list(sorted(all_species, key=lambda x: all_species[x], reverse=True))[:50]
print(len(new_head))

write_to_csv(new_head, table, 'blastn_results_matrix_sorted.csv')

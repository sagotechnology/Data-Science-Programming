import csv
from collections import defaultdict


# open the csv and read in the contents
profiles_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profiles_csv)

name_address_dict = defaultdict(str)
header = True

for row in profiles:
    
    # Skip the header again
    if header:
        header = False
        continue
    name_address_dict[row[1]] = row[5]
 
sorted_list = sorted(name_address_dict.items(), key=lambda kv: kv[1])

name_list = []

for i in range(5):
    name_list.append(sorted_list[i][0])
    
first_name_list_export = []    
for name in name_list:
    name_split = name.split(' ')
    first_name_list_export.append([name_split[0]])
    
with open('question_4.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(first_name_list_export)
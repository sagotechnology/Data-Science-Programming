import csv
from collections import defaultdict


# open the csv and read in the contents
profiles_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profiles_csv)

# Skip the first line of headers
# Using a defaultdict to count each instance of a company
name_num_dict = defaultdict(str)
header = True

for row in profiles:
    
    # skip the header again
    if header:
        header = False
        continue
    
    # Add each to a count each instance of the company name
    name_num_dict[row[1]] = row[2]

sorted_list = sorted(name_num_dict.items(), key=lambda kv: kv[1])

with open('question_5.csv', 'wt') as myfile:
    for i in range(5):
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([sorted_list[i][0]])


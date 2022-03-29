import csv
from collections import defaultdict


# open the csv and read in the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)

# Skip the first line of headers
# Using a defaultdict to count each instance of a company
profile_dict = defaultdict(int)
header = True

for row in profiles:
    
    # skip the header again
    if header:
        header = False
        continue
    
    # Add each to a count each instance of the company name
    profile_dict[row[5]] += 1

# sort country names by alphabetical order
sorted_dict = sorted(profile_dict.keys(), key=lambda kv: kv[0])
print(sorted_dict)

'''with open('filename.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(profile_list)'''


import csv
from collections import defaultdict


# open the csv and read in the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)

# Skip the first line of headers
# Using a defaultdict to count each instance of a company
country_list = []
header = True

for row in profiles:
    
    # skip the header again
    if header:
        header = False
        continue
    if row[5] not in country_list:
        # Add each to a count each instance of the company name
        country_list.append(row[5])

# sort country names by alphabetical order
country_list.sort()
country_list_export = []
for country in country_list:
    country_list_export.append([country])

with open('question_1.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(country_list_export)


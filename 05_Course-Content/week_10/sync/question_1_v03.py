import csv

# open the csv and read the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)

# Skip the first line of headers.
# Add all the different countries to a list.
country_list = []
header = True

for row in profiles:
    
    # skip the header
    if header:
        header = False
        continue
    if row[5] not in country_list:
        # Add each to a count each instance of the company name
        country_list.append(row[5])

# Sort country names by alphabetical order
country_list.sort()

# Write each item of the list to the csv as new row
with open('question_1.csv', 'wt') as myfile:
    for i in range(len(country_list)):
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([country_list[i]])

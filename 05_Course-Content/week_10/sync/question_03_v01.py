import csv

# open the csv and read in the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)


name_list = []
header = True

# Iterate through the rows of full_data.csv
for row in profiles:
    
    # skip the header again
    if header:
        header = False
        continue
    # If the address row doesn't contain a PO 
    # Split the person's name
    # Append the person's first name to name_list
    if 'P.O.' not in row[3]:
        name_split = row[1].split(' ')
        name_list.append(name_split[0])
        
name_list.sort()
    
with open('question_3.csv', 'wt') as myfile:
    for name in name_list:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow([name])
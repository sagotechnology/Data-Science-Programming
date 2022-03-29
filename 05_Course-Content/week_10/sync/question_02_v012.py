import csv

# open the csv and read in the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)


# For every different domain, append to email_list.
email_list = []
header = True

# Iterate through every row in the csv file, except for the header.
for row in profiles:
    
    # Skip the header
    if header:
        header = False
        continue
    
    # Standardize email to lowercase.
    # Split the email at @.
    # If the email domain is unique, append it to email_list.
    row_split = row[6].lower().split('@')
    if row_split[1] not in email_list:
        email_list.append([row_split[1]])

email_list.sort()

# Write every email in the list.
with open('question_2.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(email_list)

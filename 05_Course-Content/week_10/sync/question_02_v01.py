import csv
import re

# open the csv and read in the contents
profile_csv = open('full_data.csv', 'rt')
profiles = csv.reader(profile_csv)


# For every different domain, append to email_list.
email_list = []
header = True

for row in profiles:
    
    # Skip the header
    if header:
        header = False
        continue
    if row[5] not in email_list:
        email_list.append(row[6])
        
# Seprar
email_domains = []
pattern = re.compile("@")
for email in email_list:
    domain = pattern.split(email)
    if domain[1] not in email_domains:
        email_domains.append(domain[1])

email_domains.sort()

email_domains_export = []
for email in email_domains:
    email_domains_export.append([email])
    
with open('question_2.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(email_domains_export)

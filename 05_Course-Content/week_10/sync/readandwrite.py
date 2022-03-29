import csv
import json
import pickle


# function to append an item to a list within a list    
def dict_to_list_index(func_list, dictionary, key):
    for item, i in zip(dictionary[key].values(), range(len(dictionary[key]))):
        func_list[i].append(item)
    return func_list 


# CSV FILE
# open and read csv file
profile_csv_read = open('data.csv', 'rt')
profile_csv = csv.reader(profile_csv_read)

# create list and append each row is the csv file to the list
profile_list_csv = [] 

for row in profile_csv:
    profile_list_csv.append(row)
    
# JSON FILE
# open and read json file
profile_json_read = open('data.json', 'rt')
profile_dict_json = json.loads(profile_json_read.read())
profile_json_read.close()
    
    
# create list and append all the rows into the list
profile_list_json = []
# append list with [num]
for num in profile_dict_json['Name'].keys():
    profile_list_json.append([num])


# append rows to list  
dict_to_list_index(profile_list_json, profile_dict_json, 'Name')
dict_to_list_index(profile_list_json, profile_dict_json, 'Phone')
dict_to_list_index(profile_list_json, profile_dict_json, 'Address')
dict_to_list_index(profile_list_json, profile_dict_json, 'City')
dict_to_list_index(profile_list_json, profile_dict_json, 'Country')
dict_to_list_index(profile_list_json, profile_dict_json, 'Email')

   
# PICKLE FILE    
# open and read pickle file
with open('data.pkl', 'rb') as f:
    profile_dict_pickle = pickle.load(f)   
    
profile_list_pickle = []    

# append list with list num
for num in profile_dict_pickle['Name'].keys():
    profile_list_pickle.append([str(num)])

# append rows to list     
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'Name')
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'Phone')
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'Address')
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'City')
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'Country')
dict_to_list_index(profile_list_pickle, profile_dict_pickle, 'Email') 
    
# summ all the lists to one list    
profile_list = profile_list_csv + profile_list_json + profile_list_pickle

with open('filename.csv', 'wt') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(profile_list)
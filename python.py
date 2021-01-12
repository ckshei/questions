import json
# the file to be converted to  
# json format 
filename = 'data.txt'
  
# dictionary where the lines from 
# text will be stored 


list_of_lists = []

with open(filename) as fh: 
    counter = 1
    for line in fh: 
        line = line.strip('\n')
        line = line.strip('\t')
        list_of_lists.append(line[1:])


out_file = open("data.json", "w") 
json.dump(list_of_lists, out_file) 
out_file.close() 
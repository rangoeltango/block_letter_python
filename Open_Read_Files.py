### OPEN FLASH CARD & READ
# Converstion of JSON data to dictionary

# Importing the Module
import json

# Opening the JSON file
with open('FlashCardQuestions.json') as json_file:
    data = json.load(json_file)

'''print('This file has the following questions:\n')
for question in data.keys():
    print('%s' % question)
'''

#for keys, values in data.items():
#    print(values[0])

for i in data['question1']:
        print("Name:", i['name'])

'''
    # For reading nested data [0] represents the index value of the list
    print(data['question2'][0])

    # For printing the key-value pair of nested dictionary FOR loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['question1']:
        print("Name:", i['name'])
'''


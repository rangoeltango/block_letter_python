### OPEN FLASH CARD & READ
# Converstion of JSON data to dictionary

# Importing the Module
import json

# Opening the JSON file
with open('FlashCardQuestions.json') as json_file:
    data = json.load(json_file)

### This section will grab the topics from each question and print them out from a de-duped list
print('\nWelcome! We have the following topics to choose from:\n')
available_topics = []

# Getting the topics from each question
for question_info in data.values():
    topic = question_info['topic']
    available_topics.append(topic)

# Creating a de-duped list by converting into dictionary (which cannot have duplicate keys) first, then back to list
de_duped_topics = list(dict.fromkeys(available_topics))

# Printing the (unique) topics available
for topic in de_duped_topics:
    print(topic)

# Asking user which topic they would like to study
user_input = input('\nWhich topic would you like to study?')

### This section will create a temporary set of flash cards based on the user's topic selection
flashcards = []

for question, question_info in data.items():
    topic = question_info['topic']
    if user_input == topic:
        flashcards.append(question_info['question'])
    else:
        continue

for question in flashcards:
    print(question)


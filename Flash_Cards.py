### Randy's Flash Cards
import random

### WELCOME MESSAGES & OPTION TO QUIT ###
welcome = '\nWelcome to Randy\'s Flash Cards! Open License for anyone to use and/or reproduce. v0.1 May 2023'

'''
welcome += '\nTo get started, please enter your name! :)\n'

# Asking for username and defining authorized guests
user_name = input(welcome)
authorized = ('Randy', 'Reggie', 'Guest')

# Auth check (will need to nest in here)
if user_name in authorized:
    print('You shall pass %s.' % user_name)
else: 
    print('Access denied. :(')
'''

# Defining possible topics & selection messages
topics = ['Python', 'Plants', 'Pets']
topic_list = ''

instructions = '\nTo get started, please select a topic!'
instructions += '\nYour choices are:\n%s\n' % topics

# Prompt user for a topic with the above instructions
topic_selection = input(instructions)

# Check to see if selected topic is valid to either stop or continue
while topic_selection in topics:
    print('%s is a great choice! Let\'s get started...' % topic_selection)
    break
else: 
    print('I don\'t recognize your topic selection and have decided to quit in protest.')




'''
class UserSession:
#A session instance to store information about a new/ongoing flash card sesh!

### INCOMPLETE ###

# def __init__(self):
        self.user_name = user_name'''

class FlashCard:
    '''A General Flashcard Template'''

    def __init__(self, topic, type, name, question, choices, answer):
        self.topic = topic
        self.type = type
        self.name = name
        self.question = question
        self.choices = choices
        self.answer = answer
    
    def print_question(self):
        print('\n##### QUESTION - %s #####\nThis is a %s question. Good luck! %s\n' % (self.name, self.topic, self.question))
    
    def print_choices(self):
        print('%s\n' % self.choices)
    
    def print_answer(self):
        print('The correct answer is %s.' % self.answer)

# Flashcard Questions
# FlashCard(self, topic, type, name, question, choices, answer, user_input)
question1 = FlashCard('Python', 'Multiple Choice', 'TUPLES', 'QUESTION: Tuples are declared with ______ & are ______','(A) [], mutable\n(B) [], immutable\n(C) (), mutable\n(D) (), immutable', 'D', '')

#question1.print_question()
#question1.print_choices()


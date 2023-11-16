### Trivia program
## THIS PROGRAM IS STILL BEING DEVELOPED AND IS INCOMPLETE
## CURRENTLY SET TO HIT trivia.txt in directory for default load file.



### This program will load trivia questions of a specific format into a program to ask them to you like flash cards!
import time

print("Hey there! Welcome to Randy's trivia slash flash cards program!\n")
time.sleep(0.5)
print("Are you ready to rumble?\n")
time.sleep(0.5)
fname = input("To start things off, which trivia file would you like to load?")

## Default to a sample text file I have saved if no name is entered
if len(fname) < 1:
    fname = 'trivia.txt'

## Error handling around actual file opening
try:
    fhand = open(fname)
except:
    print("\n\n......\n\nThat is unfortunately a bad file name, my trivia amigo/amiga. Check the directory and file name and try again!")
    print("Don't forget to include the file extension!\n\n.........\n")

## Establishing an empty dictionary to store key:counts
countsdict = dict()
## Establishing empty lists for the question parts
questions = list()
qtypes = list()
choices = list()
answers = list()
## Setting a list of expected row prefix syntax
prefixes = ['Question:', 'Type:', 'Choices:', 'Answer:']

## Going through each line in the file
for line in fhand:
    line = line.rstrip()
    ## Checking for lines with the chosen prefix words, and keeping ONLY those lines as our dataset
    if not line.startswith(tuple(prefixes)):
        continue
    elif line.startswith('Question:'):
        questions.append(line)
    elif line.startswith('Type:'):
        qtypes.append(line)
    elif line.startswith('Choices:'):
        choices.append(line)
    elif line.startswith('Answer:'):
        answers.append(line)
print("\nWoo, loading complete!\n")
time.sleep(0.5)
print("It looks like there are:",len(questions),"questions available!\n")
time.sleep(0.5)

## Asks the user to select a question number
print("Choose a number between 1 and ",len(questions))
choice = input("")

## Asks for user input and tries until they enter a number within the range
while (int(choice)-1) not in range(len(questions)):
    print("Uh oh! Looks like that isn't one of the number options... try again?")
    choice = input("")
    continue
## Setting the user choice and index to match (starting at 1 instead of 0)
choice = int(choice) -1


activequestion = questions[choice]
activechoice = choices[choice]
activeanswer = answers[choice]
activeqtype = qtypes[choice]

# QUESTION PRINTING STUFF
# Taking the chosen question and splitting it to look at just the raw type
q = activeqtype.split()
qtype = q[1]

# Prompting the user with the type of choice with additional details
if qtype == "MultipleChoice":
    qprompt = "Multiple Choice! When you are ready, type in the letter of your guess and hit (ENTER)...\n"
elif qtype == "TrueFalse":
    qprompt = "True or False! Type in T or F and hit (ENTER) to guess...\n"
elif qtype == "Text":
    qprompt = "Text guess! Type in your answer and hit (ENTER)...\n"

# Prints out the question type information, the question, and the choices
print("\nThis question type is", qprompt)
time.sleep(0.5)
print(activequestion)
time.sleep(0.5)
print(activechoice)

# Takes a guess from the user
userguess = input("\nEnter your guess:")

if  qtype == "MultipleChoice":
    # Stuff prepping answer letter
    a = activeanswer.split()
    aparen = a[1]
    aprenpieces = list(aparen)
    answerletter = aprenpieces [1]
    # Stuff prepping answer from choices
    cwords = activechoice.split()
    wordplace = 0

    for word in cwords:
        if word != aparen:
            wordplace += 1
            continue
        elif word == aparen:
            answer = cwords[(wordplace+1)]
            break

    if userguess == answerletter:
        print("That is correct! It was", answer,"!")
    else:
        print("\nBzZzZzZztttt! Sorry that is incorrect")
        print("The correct answer was", aparen, answer,"\n")

elif qtype == "TrueFalse":
    print("")
elif qtype == "Text":
    print("")
else: 
    print("Error in qtype, QUEEN!")

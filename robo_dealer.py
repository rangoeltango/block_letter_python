############################################
####        Randy's Card Machine        ####
############################################
# Modules that I think can spice this thing up or customize:
# import random             # You already know what this does
# from time import sleep    # This bad boy can add time breaks between prints

## Defining my printing function
def card_print(card_num, row_len_max=5, card_type='X'):
    full_row_num = card_num // row_len_max
    final_row_len = card_num % row_len_max

    card = " ["+card_type+"] "
    full_row = row_len_max * card
    final_row = final_row_len * card

    while full_row_num > 0:
        print(full_row)
        full_row_num -= 1
    if final_row_len > 0:
        print(final_row)

## Indefinite loop to allow multiple uses until quitting
while True:
    user_choice = input("\nWelcome! Would you like to print some cards? (Y/N)  ")
    if user_choice.strip() != 'y' and user_choice.strip != 'Y':
        break
    
    ## Number of Cards input and error handling
    while True:
        try:    
            user_card_num = int(input("\nHow many cards would you like to lay out?  "))
            if user_card_num < 1:
                print("\n***** Sorry but you need at LEAST one card otherwise what is this all about? *****")
                continue
            break
        except:
            print("\n***** Sorry but that didn't look like a number to me, can you try again? *****")

    ## Row Length input and error handling
    while True:
        try:
            user_row_len = int(input("\nGreat! Now, how long would you like each row of cards to be?  "))
            if user_row_len < 1:
                print("\n***** *Miming laying out invisible cards* There you go wisecrack!  *****")
                print("\n***** Seriously though, you need at least 1 card per row otherwise I have no clue what you want. *****")
                continue
            if user_row_len > user_card_num:
                print("\nThat's shorter than the total number of cards, one REALLY nice row coming up!")
                break
            break
        except:
            print("\n***** Sorry but that didn't look like a number to me, can you try again? *****")

    ## Card Pattern input and error handling
    while True:
        try:
            user_card_type = input("\nIf you want a specific pattern on the back enter it here otherwise hit enter to skip:  ")
            if len(user_card_type) < 1:
                user_card_type = " "
            break
        except:
            print("***** I wasn't even sure if it was possible to throw this error, so congrats! *****")

    ## Actual Card Printing
    print("\nWatch out! Here they come:   \n")
    card_print(user_card_num, user_row_len, user_card_type)
    print("\nHow's that for some cards? Woo!\n")

## Goodbye!
print("\n***** Thank you very much for trying this out! ****\n")
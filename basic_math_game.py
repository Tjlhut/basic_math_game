from random import randint, choice
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%d/%m/%Y")
file_name = "math_game_log.txt"

# Functions

def append_wrong_answer(answer,operation,file_name=file_name):
    with open(file_name, 'a') as f:
        f.write(f'\tExpression: {operation}, User Input: {answer}, '\
            f'Expected: {eval(operation)}\n')

def check_if_int(answer):
    '''Checks if the input is an integer. '''
    try:
        int(answer)
    except ValueError:
        print('Your answer cannot contain anything other than numbers. Please try again: ')
        return False

    else:
        return True

def addition(a, b):
    operation = f"{a} + {b}"
    answer = input(operation + ' = ')

    while check_if_int(answer) == False:
        answer = input ('\n'+operation + ' = ')

    if eval(operation) == int(answer):
        return('Excellent!')

    else:
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')


def subtraction(a, b):
    if difficulty == 'easy':
        while b>a:
            x1,x2 = difficulty_lvls['easy'][0][0], difficulty_lvls['easy'][0][-1]
            a, b= randint(x1, x2), randint(x1, x2)

    operation = f"{a} - {b}"
    answer = input (operation + ' = ')

    while check_if_int(answer) == False:
        answer = input ('\n'+operation + ' = ')

    if eval(operation) == int(answer):
        return(f'Correct! Well done, {name}.')
    else:
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')


def multiplication(a, b):
    operation = f"{a} * {b}"
    answer = input(operation + ' = ')

    while check_if_int(answer) == False:
        answer = input ('\n'+operation + ' = ')
    if eval(operation) == int(answer):
        return(f'Good job, {name}!')
    else: 
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')

#                           *Actual game:*

"""For the dictionary below:
The first element of each list is the smallest possible number to be used
the second is the largest possible number. The first list is for the addition and
subtraction questionss, the second is for the multiplication questions."""

difficulty_lvls = {
    'easy': [[5, 30], [2, 11]],
    'intermediate': [[10, 50], [3, 12]],
    'difficult':[[12,100],[4, 17]],
    'expert': [[30, 2000], [6, 30]],
    }

name = input('Please enter your name: ').title()
difficulty = input("Difficulty level (easy, intermediate, difficult, expert): ")
while difficulty not in difficulty_lvls:
    difficulty = input("\nYou chose a non-existent level."\
        "Please try again(easy, intermediate, difficult, expert): ")

#     while False
# while difficulty in difficulty_lvls == False:
    # difficulty = input("\nYou chose a non-existent level."\
    #     "Please try again(easy, intermediate, difficult, expert): ")

with open(file_name) as f:
    contents = f.read()

with open(file_name, 'a') as f:
    if current_time not in contents:
        f.write(current_time + ': \n')      
    f.write('\n'+name+':')
    f.write('\n\t'+difficulty.title()+'\n')

lst = ['addition', 'subtraction', 'multiplication']

greeting = (f"\nHello, {name}. You'll be given a chance to exit this program "\
" and level up after every 5 attempts. Let's begin! \n")
print(greeting)

i = 0
while True:

    if i%5==0:
        d=difficulty
        x1,x2=difficulty_lvls[d][0][0], difficulty_lvls[d][0][-1]
        y1,y2=difficulty_lvls[d][-1][0], difficulty_lvls[d][-1][-1]
# The issue here is that randint does not accept ranges
    a1,a2 = randint(x1, x2), randint(x1, x2)
    m1,m2 = randint(y1, y2), randint(y1, y2)

    '''Randomizer'''
    chosen = choice(lst)

    if chosen == lst[0]:
        print(addition(a1, a2))
    elif chosen == lst[1]:
        print(subtraction(a1, a2))
    else: 
        print(multiplication(m1, m2)) 
    
    i+=1

    if i %5 == 0:
        print('\n')
        answer = input(f'Would you like to continue, {name}? (yes/no) ')
        if answer == 'no':
            break
# Here we ask if the user wants to go on to the next level. We must first
# check if the user is not currently at the last level as there is no lvl to lvl up to.
        if difficulty in list(difficulty_lvls.keys())[:-1]:
            lvl_up = input("Would you like to advance to the next level? (yes/no) ")
            if lvl_up == 'yes':
                next_index = list(difficulty_lvls.keys()).index(difficulty)+1
                difficulty = list(difficulty_lvls.keys())[next_index]
                print(f"\nNew difficulty level: {difficulty.title()}\n")
                with open(file_name, 'a') as f:
                    f.write('\n\t'+difficulty.title()+'\n')

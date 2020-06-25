from random import randint, choice
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%d/%m/%Y")
file_name = "math_game_log.txt"


# Functions

def append_wrong_answer(answer,operation,file_name=file_name):
    with open(file_name, 'a') as f:
        f.write(f'\tIncorrect answer: {operation}, Actual: {answer}, '\
            f'Expected: {eval(operation)}\n')

def check_if_int(answer):
    '''Check if the input is an integer. We need to ignore negative signs
    as they fail the .isdigit() test. '''
    if answer[0]=='-':
        answer = answer[1:]
    return answer.isdigit()


def must_return_int(answer, operation):
    print('Your answer cannot contain anything other than numbers. Please try again: ')
    print(operation)
    answer = input ('\n'+operation + ' = ')
    return answer




def addition(a, b):
    operation = f"{a} + {b}"
    answer = input(operation + ' = ')
    # while check_if_int(answer)== False:
    #     print('Your answer cannot contain anything other than numbers. Please try again: ')
    #     operation = f"{a} + {b}"
    #     answer = input ('\n'+operation + ' = ')
    while check_if_int(answer) == False:
        must_return_int(answer, operation)
    if eval(operation) == int(answer):
        return('Excellent!')
    else:
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')


def subtraction(a, b):
    if difficulty == 'easy':
        while b>a:
            x1 = difficulty_lvls.get('easy')[0][0]
            x2 = difficulty_lvls.get('easy')[0][-1]
            a = randint(x1, x2)
            b = randint(x1, x2)
    operation = f"{a} - {b}"
    answer = input (operation + ' = ')
    # I've got an issue here, negative inputs fail the .isdigit() test
    while check_if_int(answer)== False:
        print('Your answer cannot contain anything other than numbers. Please try again: ')
        operation = f"{a} - {b}"
        answer = input ('\n'+operation + ' = ')

    if eval(operation) == int(answer):
        return(f'Correct! Well done, {name}.')
    else:
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')


def multiplication(a, b):
    operation = f"{a} * {b}"
    answer = input(operation + ' = ')
    while check_if_int(answer)== False:
        print('Your answer cannot contain anything other than numbers. Please try again: ')
        operation = f"{a} * {b}"
        answer = input ('\n'+operation + ' = ')
    if eval(operation) == int(answer):
        return(f'Good job, {name}!')
    else: 
        append_wrong_answer(answer, operation)
        return(f'Incorrect. The correct answer is {eval(operation)}.')

# def division(a, b):
#     division = f"{a} / {b}"
#     while a%b !=0:
#         y1 = difficulty_lvls.get(difficulty)[-1][0]
#         y2 = difficulty_lvls.get(difficulty)[-1][-1]
#         b = randint(x1, x2)
#     answer = input(division + ' = ')
#     while answer.isdigit() == False:
#         print('Your answer cannot contain anything other than numbers. Please try again: ')
#         division = f"{a} / {b}"
#         answer = input ('\n'+division + ' = ')
#     if int(eval(division)) == int(answer):
#         return(f'Good job, {name}!')
#     else:
#         return(f'Incorrect. The correct answer is {int(eval(division))}.')

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

with open(file_name) as f:
    contents = f.read()

with open(file_name, 'a') as f:
    if current_time not in contents:
        f.write(current_time + ': \n')
    # if name not in contents:
    f.write('\n'+name+': \n')
    f.write('\t'+difficulty+'\n')

lst = ['addition', 'subtraction', 'multiplication']

while difficulty in difficulty_lvls == False:
    difficulty = input("\nYou chose a non-existent level."\
        "Please try again(easy, intermediate, difficult, expert): ")

greeting = (f"\nHello, {name}. You'll be given a chance to exit this program "\
" and level up after every 5 attempts. Let's begin! \n")
print(greeting)

i = 0
while True:

    if i%5==0:
        x1 = difficulty_lvls.get(difficulty)[0][0]
        x2 = difficulty_lvls.get(difficulty)[0][-1]
        y1 = difficulty_lvls.get(difficulty)[-1][0]
        y2 = difficulty_lvls.get(difficulty)[-1][-1]
# The issue here is that randint does not accept ranges
    a1 = randint(x1, x2)
    a2 = randint(x1, x2)
    m1 = randint(y1, y2)
    m2 = randint(y1, y2)

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
                    f.write("--"+difficulty+"--\n")


# print("Oof, doesn't look like you're doing so well. Would you like to change the difficulty level?")
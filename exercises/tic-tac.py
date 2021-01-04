def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

print(row1,row2,row3)

position_index = int(input('Please enter a value: '))

def user_choice():

    choice = 'WRONG'

    while choice.isdigit() == False:

        choice = input('Please enter a number (0-10): ')

        if choice.isdigit() == False:
            print('Sorry that is not a number.')

    return int(choice)

print(user_choice())

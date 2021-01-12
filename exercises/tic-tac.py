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

    # Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number (0-10): ')

        # digit check
        if choice.isdigit() == False:
            print('Sorry that is not a number.')

        #range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry that number is out of the acceptable range 1-10.")
                within_range = False

    return int(choice)

print(user_choice())

result = 'WRONG VALUE'
acceptable_values = [0,1,2]

result not in acceptable_values

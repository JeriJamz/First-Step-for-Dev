choice = input('Yes or No?: \n')
#duuuuuude some this is a better version of data validation

match choice:
    case 'Yes':
        print('Yes :)')
    case 'No':
        print('No :(')
    case _:
        print('You entered something else!')

todo_list = {'Sunday' : '', 'Monday' : '', 'Tuesday' : '', 'Wednesday' : '',
             'Thursday' : '', 'Friday' : '', 'Saturday' : ''}
user_input = ''
while user_input != 'quit':  
    user_input = input('Prompt: What would you like to do?\n>')
    if user_input == 'add':
        day = input('What day?\n>').capitalize()
        advance = day in todo_list
        if advance == 1:
            print('\nPrompt: What would you like to add to', day + "'s",
                  'to-do list?', end = '')
            todo_list[day] = todo_list[day] + 'You have to ' + input('>') \
            + '.' + '\n\t  '
        else:
            print('Invalid entry - please enter a correct day of the week\
(like Monday or monday)')
    elif user_input == 'get':
        day = input('Prompt: What day?\n>').capitalize()
        print('\nResponse:',todo_list.get(day, 'Invalid entry - please\
 enter a correct day of the week (like Monday or monday)'))
    elif user_input == 'quit':
        print('\nResponse: Ending program. Thank you for using the to-do list!')
    else:
        print("'"+ user_input + "'", 'not supported')

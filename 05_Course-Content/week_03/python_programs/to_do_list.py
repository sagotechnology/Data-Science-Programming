todo_list = {'sunday' : [], 'monday' : [], 'tuesday' : [], 
             'wednesday' : [],'thursday' : [], 'friday' : [],
             'saturday' : []}
user_input = ''
while user_input != 'quit':  
    user_input = input('Prompt: What would you like to do?\n>')
#add to the todo list
#
    if user_input == 'add':
#loop until a valid day is entered
        loop = 0
        while loop != 1:
            day = input('What day?\n>').lower()
            loop = day in todo_list
            advance = loop
            if not advance:
                print('Invalid entry - please enter a correct day of the week \
(like Monday or monday).')
#valid day is entered 
        print('\nPrompt: What would you like to add to', day.capitalize() + "'s",
                  'to-do list?', end = '')
        todo_list[day].append(input('>'))
#get from the todo list
#
    elif user_input == 'get':
#loop until a valid day is entered        
        loop = 0
        while loop != 1:
            day = input('What day?\n>').lower()
            loop = day in todo_list
            advance = loop
            if not advance:
                print('Invalid entry - please enter a correct day of the week \
(like Monday or monday).')
#valid day is entered, loop until all items in list are printed                
        i = 0
        j = len(todo_list[day])
        print('')
        while i < j:
            print('Response: You have to',todo_list[day][i])
            i += 1
#quit the program            
    elif user_input == 'quit':
        print('\nResponse: Ending program. Thank you for using the to-do list!')
#input not defined
    else:
        print("'"+ user_input + "'", 'not supported')
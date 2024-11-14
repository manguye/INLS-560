import sys # Don't use quit() or exit() in production code. Use sys.exit

# Make program repeat.
while True:

# Get user input for file.
    file_variable = input('''
        What file would you like to search for?:
        a) 60s-music file
        b) athletes file
        x) to exit
        ''')
    
# Process user input.
    if file_variable == 'x':
        sys.exit() # This requires
    elif file_variable == 'a':
        file_variable = 'assignment_08/60s_music.csv'
    elif file_variable == 'b':
        file_variable = 'assignment_08/athletes.csv'
    else:
        print('Invalid option. Please select a, b, or x.')
        continue

    # Enter a search term; this is a global variable.
    search_variable = input(f'Enter the search term for {file_variable} file: ')
    search_variable = search_variable.title() # Capitalizes first letter of search.

    # Go to 02_search_for_term.py to continue(?)
    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file:
            content = file.read()
    # Now the file is in the memory buffer as content.

    # Next check to see if the search_variable is in the content buffer:
        if search_variable in content:

        # If the file prints that it is in the file AND
        # If the user wants to see the entries for the term:
            print(f'Your search term {search_variable} exists in the {file_variable} file!')
            see_entries = input('Would you like to see the entries? (y or n)?')

            # If y then run this code to output all the entries:
            if see_entries.lower() == 'y':
                print(f'Here are all of the entries with the term {search_variable}:')
                with open(file_variable, 'r') as file:
                    for line in file:
                        if search_variable in line:
                            print(line.strip())
        
            # If n, then run this code.
            elif see_entries.lower() == 'n':
                print('Goodbye')
                sys.exit()

            else:
                print('Invalid option. Please enter y or n.')

        # If search_variable is not there, say so.
        else:
            print(f'{search_variable} does not exist in {file_variable}')

    # Call the function.
    find(file_variable, search_variable)


    
menu_option = ''
while menu_option != 'q':
    print('MENU:', 'a: specialty cakes', 'b: cookies',
           'q: quit', sep="\n")
    menu_option = input('Enter a letter for more info about our bakery!: ')
    if menu_option == 'a':
        print('We cater for nearly any event with nearly any design!')
    elif menu_option == 'b':
        print('With or without milk, these cookies are positively scrumptious!'
              )
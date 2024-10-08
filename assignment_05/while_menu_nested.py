menu_option = ''
while menu_option != 'q':
    print(f'''
          Shop information FAQS:
          a: specialty cakes
          b: cookies
          q: exit
          ''')
    menu_option = input('Enter a letter for more info about our bakery!: ')
    if menu_option == 'a':
        print('We cater to nearly any event with nearly any design!')
    elif menu_option == 'b':
        milk = input('Do you eat your cookies with milk? Enter (y or n): ')
        if milk == 'y':
            print('Just like Santa Claus!')
        else:
            print('Hardcore.')
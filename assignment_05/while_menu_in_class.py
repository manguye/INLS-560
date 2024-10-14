menu_option = ''

while menu_option != 'q':
    print(f"""
          BurgerHaus Menu:

          a - Cheeseburger ($5)
          b - Double Cheeseburger ($7)
          c - Dosa ($6)
          d - Milkshake ($4)
          e - Mac and Cheese ($3)
          f - Biryani ($8)
          q - Quit

          Please enter a letter: 
          """)
    
    menu_option = input("> ")

    if menu_option == 'a':
        print("You ordered a Cheeseburger!")

    elif menu_option == 'b':
        print("You ordered a Double Cheeseburger!")

    elif menu_option == 'c':
        print("You ordered a Dosa!")

    elif menu_option == 'd':
        wants_shake = input(
            'What flavor? (v)anilla, (s)trawberry, or (c)hocolate: '
                            )
        if wants_shake == 'v':
            print("You ordered a vanilla milkshake!")
        elif wants_shake == 's':
            print("You ordered a strawberry milkshake!")
        elif wants_shake == 'c':
            print("You ordered a chocolate milkshake!")
        else:
            print("Sorry! Invalid flavor option!")

    elif menu_option == 'e':
        print("You ordered a Mac and Cheese!")

    elif menu_option == 'f':
        print("You ordered a Biryani!")

    elif menu_option == 'q':
        print("Thank you for ordering!")

    else:
        print("Sorry! Invalid menu option!")
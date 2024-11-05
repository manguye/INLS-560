# Experimenting with try, except, else, and finally in Python.

title = 'Python in easy steps'

try:
    print(titel)

except NameError as msg:
    print(msg)

else:
    print('Nothing went wrong.')

finally:
    print('Try finished checking.')
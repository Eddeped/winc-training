# type exercise
type (3)
type (3.14)
type ('pi')
# If we assign a value to a variable we can ask Python what the type of the value in that variable is:
some_number = 5
type(some_number)
another_number = 9.81
type(another_number)
some_string = 'Hello world'
type(some_string)
test='hallo it\'s me, hoppa\\t \t use the "backslash" (\)\
and we continue on the \
next code line'
test2="but to do an actual next line use \\n like this \n next line \u0167"
print (test)
print (test2)
print('''this can be over 
multiple lines and have " and ' in them''')

waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
waltz[0:11:2]

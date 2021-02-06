def repeat_lyrics():
    print_lyrics()
    print_lyrics()  #Functions that are not defined can be called
                    #Before they are declared

def print_lyrics():

    print('Here we go round the mulbery bush')
    print('I am sleep all night and I have work to do')

repeat_lyrics()

#Need to ensure function is not used before it is defined.

def print_twice(value):
    print(value)
    print(value)

print_twice('spam ' * 4) 


def cat_twice(part1, part2):
    cat = part1 + part2 #Concatenates the program
    print_twice(cat)

cat_twice('hello', 'world')

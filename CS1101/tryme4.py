#The main function to print one (1) line.
def new_line(): 

    print('.') #A dot for visual assessments



#Function to print 3 single lines.
def three_lines():

    # Call the the main function three times.
    new_line()

    new_line()

    new_line()
    # This will print three lines



#Function to print 9 single lines.
def nine_lines():

    # Call the three_lines function three times.
    three_lines()

    three_lines()

    three_lines()
    # Consecutively calling three lines
    # Prints 3 * three_lines = 9 lines


#Function to print 25 lines
def clear_screen():

    # Call nine_lines
    nine_lines() # 9 lines 
    nine_lines() # 9 lines

    #Call three_lines
    three_lines()# 3 lines
    three_lines()# 3 lines

    new_line();  # 1 line
    #----------------------
    # Total -----> 25 line



print('printing nine lines') #Placeholder
nine_lines() #Print 9 lines


print('calling clearScreen') #Placeholder
clear_screen() #Print 25 lines

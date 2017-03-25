# Python:   2.7.13
#
# Author:   Nash N. Wood
#
#Purpose:   The Tech Academy - Python Course, Item 36 
#           Demonstrating how to perform various tasks in Python
#
#===============================================================#




#1. Assign an integer to a variable


var_int = 4


#2. Assign a string to a variable


var_string = "This is a string."


#3. Assign a float to a variable


var_float = 4.3561


#4. Use the print function and .format() notation to print out the variable you assigned  


print "{}".format(var_string)


#5. Use each of these operators +, - , * , /, %,([+=, -=] <--found in #8.)


1 + 2
14 - 3
8 * 7
16 / 4
3 % 1


#6. Use of logical operators: and, or, not


if (self.a != 0) and (self.b != 0) :
    if (self.a != 0) or (self.b != 0) :
if 0 not in (self.a, self.b) :


#7. Use of conditional statements: if, elif, else


def like_dogs(decision):

    decision = raw_input("Do you like dogs?\nYes/No").capitalize()
    if decision == "Yes":
        print("A fellow dog lover!")
    elif decision == "No":
        print("Perhaps cats are more your type?")
    else:
        print("I'm going to need a straight answer.")

like_dogs(decision)


#8. Use of a while loop


counter = 0

while counter < 5:
                print counter
                counter += 1

downcounter = 5

while downcounter > 0:
                print downcounter
                downcounter -= 1
                

#9. Use of a for loop


for x in range(0, 3):
    print "We're on time %d" % (x)


#10. Create a list and iterate through that list using a for loop to print each item out on a new line


counter = 0

for counter in range(0,5):
                print counter
                
#11. Create a tuple and iterate through it using a for loop to print each item out on a new line


tuple1 = (1,2,3,4,5)

for tuple1 in range(1,6):
        print tuple1
        

#12. Define a function that returns a string variable


name = ""

def describe_game(name):
    if name != "": 
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.")
                    print("You can be nice or mean when interacting with them.")
                    print("At the end of the game your fate will be decided from your actions.")
                    stop = False
    return name        


#13. Call the function you defined above and print the result to the shell


describe_game(name)
print(name)






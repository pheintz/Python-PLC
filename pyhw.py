# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

'''
    Patrick Heintz
    Programming Language Concepts
    HW4
'''

#   Price of boards
boards = 21.99
#   Sales Tax
tax = 1.09
#   Meters per second
gravity = 9.8
'''
    Problems 1-4 in the python section of assignment # 4
'''
def main(argv=None):
    problemOne()
    problemTwo()
    problemThree()
    problemFour()


'''
    1) An electronics company sells circuit boards that cost $21.99. 
    Assume tax is 9%.  Print the total price of 3 circuit boards
'''
def problemOne():
    price = boards * 3 * tax
    print ("$ %.2f is the price of 3 boards" % price)
    
    

def problemTwo():
    grade = int(input("What was your % grade?\n"))
    
    if grade <= 100 and grade >=0:
        if grade > 90:
            print("You got an A")
        elif grade > 80:
            print("You got a B")
        elif grade > 70:
            print("You got a C")
        elif grade > 60:
            print ("You got a D")
        else:
            print ("You got an F")
    else:
        print("Not a possible grade...")
        problemTwo()
        
def problemThree():
    weight = float(input("Enter an object's mass in KG and I'll give you the weight in newtons\n"))
    weight = weight * gravity
    if weight > 1000:
        print("The object weighs %.2f Newtons.  It is very heavy" % weight)
    else:
        print("The object weighs %.2f Newtons.  It is very light" % weight)

'''
    4) Using the following names: 
    Kerry, Thomas, Marina, Kevin, Jose, Gina, Josephine.  
    Write a program that prints only the names that begin with J or K.
'''
def problemFour():
    names = ["kerry", "thomas", "marina", "kevin", "jose", "gina", "josephine"]
    for x in names:
        if x[0] == 'k':
            print(x)
        if x[0] == 'j':
            print(x)
            
    
if __name__ == "__main__":
    main()
    exit()
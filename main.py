#function that adds two numbers together
def add(x,y):
    print(x+y)

#function that subtracts two numbers
def sub(x,y):
    print(x-y)


#multiply two numbers together
def mult(x,y):
    print(x*y)


#divide two numbers
def div(x,y):
    print(x/y)





print("Welcome to the calculator app, your favorite place to retreat to pretend your doing something when people your age walk by! :)")

while True:

    print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (g)ive up like a baby")
    user_choice = input("I want to... ")
    print("You chose", user_choice)

    if user_choice == 'a':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add(x,y)

    elif user_choice == 's':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        sub(x,y)

    elif user_choice == 'm':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        mult(x,y)

    elif user_choice == 'd':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        div(x,y)

    if x == 99:
        print("A batch of genetically enhanced clones. We call them clone force 99. The Bad Batch.")
    if y == 99:
        print("A batch of genetically enhanced clones. We call them clone force 99. The Bad Batch.")

    elif user_choice == 'g':
        print("Loser, you give up this quick? You will never make it you absolute disgrace.")
        break
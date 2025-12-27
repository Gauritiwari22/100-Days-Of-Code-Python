# "Day3"

# Conditional statements
print("Welcome to roller coaster!")
height=int(input("What is your height in cm:"))
if height> 120:
    print("Eligible for roller coaster")
else:
    print("Not eligible for the roller coaster")

# # comaprison operators: >,<,==,>=,<=,!=

# #modulo operator- returns remainder after divison
print(10%5) #0
print(10%3) #1

# #Code to check whether number is odd or even
num=int(input("Enter a number:"))
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")


#conditional statements using nested if statemnets

print("Welcome to roller coaster!")
height=int(input("What is your height in cm:"))
age=int(input("How old are you? "))
if height> 120:
    print("Eligible for roller coaster")
    if age<=18:
        print("You need to pay $7 for the ride")
    else:
        print("You need to pay $10 for the ride")
else:
    print("Not eligible for the roller coaster")

#using elif

print("Welcome to roller coaster!")
height=int(input("What is your height in cm:"))
age=int(input("How old are you? "))
if height> 120:
    print("Eligible for roller coaster")
    if age<=12:
        print("You need to pay $5 for the ride")
    elif age<=18:
        print("You need to pay $7 for the ride")
    else:
        print("You need to pay $10 for the ride")
else:
    print("Not eligible for the roller coaster")


# multiple if statements in succession
print("Welcome to roller coaster!")
height=int(input("What is your height in cm:"))
age=int(input("How old are you? "))
photo=str(input("Do you also want a photo of yourself on the ride? yes/no"))
bill=0

if height> 120:
    print("Eligible for roller coaster")
    if age<=12:
        bill=5
        print("You need to pay $5 for the ride")
    elif age<=18:
        bill=7
        print("You need to pay $7 for the ride")
    else:
        bill=10
        print("You need to pay $10 for the ride")
    if photo=="yes":
        #add extra $3 in the bill
        bill+=3
    print(f"your final bill is ${bill}")
    

else:
    print("Not eligible for the roller coaster")


#pizza order practice
print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S,M or L:")
pepperoni=input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese=input("Do you want extra cheese? Y or N:")
amount=0

if size=="S":
    amount+=12
elif size=="M":
    amount+=15
elif size=="L":
    amount+=20
else:
    print("Input correct size")


if pepperoni=="Y":
        if size=="S":
            amount+=3
else:
        amount+=5


if extra_cheese=="Y":
        amount+=4
      

print(f"Your total bill is ${amount}")


# Logical operators
# and- all conditions must be True
# or- atleast one condition must be true
a=10
a>5 and a<15 #output=True
a>5 or a<9 #output=true
True or False #output=True




print("Welcome to roller coaster!")
height=int(input("What is your height in cm:"))
age=int(input("How old are you? "))
photo=str(input("Do you also want a photo of yourself on the ride? yes/no"))
bill=0

if height> 120:
    print("Eligible for roller coaster")
    if age<=12:
        bill=5
        print("You need to pay $5 for the ride")
    elif age<=18:
        bill=7
        print("You need to pay $7 for the ride")
    elif age>=45 and age<=55:
        bill=0
        print("yay! You have a free ride")
    else:
        bill=10
        print("You need to pay $10 for the ride.")
    if photo=="yes":
        #add extra $3 in the bill
        bill+=3
    print(f"your final bill is ${bill}")
    

else:
    print("Not eligible for the roller coaster")
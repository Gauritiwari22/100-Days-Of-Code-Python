"Day8"

#Functions review
def greet():
    print("Hello!")
    print("How are you doing?")
    print("Where are you going?")
    
greet()

# Function with inputs
def greeting(name):
    print("Hello",name)
    print(f"How are you doing {name}")
greeting("Gauri") # here name is the parameter and Gauri is the argument

def life_in_weeks(age):
    total_weeks=90*52
    weeks_lived=age*52
    weeks_left=(total_weeks-weeks_lived)
    print(f"You have {weeks_left} weeks left.")
life_in_weeks(5)

# Functions with more than 1 input - positional arguments
def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"Welcome to {location}")

greet_with("Gauri","India")

# Keyword arguments
def greet_like(name="Gauri",location="India"):
    print(f"Hello {name}!")
    print(f"Welcome to {location}")
greet_like()

# Love calculator
def calculate_love_score(name1="yashwardhan", name2="hitakshi"):
    
    count1 = 0
    for i in "true":
        if i in name1:
            count1 += 1
        if i in name2:
            count1 += 1

    count2 = 0
    for j in "love":
        if j in name1:
            count2 += 1
        if j in name2:
            count2 += 1

    total = str(count1)
    love = str(count2)

    print("Your total love is:", total + love)


calculate_love_score()



    
    




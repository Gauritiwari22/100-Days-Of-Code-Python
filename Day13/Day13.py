"Day13"

# Debugging
def my_function():
    for i in range(1,20):
        if i==20:
            print("You got it!")
my_function()

# here is the above program, on checking closely we see that nothing gets printed on calling the function
# because when we use the for loop to iterate over the range of numbers, it never reaches 20, because
# range(1,20) means numbers from 1 to 19 i.e 20 is excluded hence i never equals 20. Hence, nothing gets printed

"Corrected version"
def my_function():
    for i in range(1,21): # range of numbers from 1 to 20
        if i==20:
            print("You got it!")

my_function()

year=int(input("What is your year of birth?: "))
if year>1980 and year<1994:
    print("You are a Milleninal")
elif year>1994:
    print("You are a Gen-Z")

# If we input the year as 1994, on executing nothing will get printed as 1994 is not included in any
# of the if-elif conditions hence the computer does not print anything.

"Corrected version"
year=int(input("What is your year of birth?: "))
if year>1980 and year<1994:
    print("You are a Milleninal")
elif year>=1994: # 1994 is included
    print("You are a Gen-Z")


age=input("Enter your age: ")
if age>18:
    print("Adult")
else:
    print("Minor")

# If we input any numeric value like 45, 23, 10 etc, there will be an error shown in the console.
# by default, the input function takes string values and hence you cannot compare string values to
# integers. Therefore, for comparison similar data types shall be considered.

"Corrected version"
age=int(input("Enter your age: ")) # converted the input vales to integer
if age>18:
    print("Adult")
else:
    print("Minor")

"OR"

# Using Exception handling
try:
    age=int(input("Enter your age: ")) 
except ValueError:
    print("You have typed in an invalid number. Try again with a numerical value:")
    age=int(input("Enter your age: ")) 

    if age>18:
        print("Adult")
    else:
        print("Minor")

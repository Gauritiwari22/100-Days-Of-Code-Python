# # ERRORS

# #TypeError
# word="hello"
# print(word+5)

# #IndexError
# fruits=["apple","mango","banana"]
# print(fruits[4])

# #KeyError
# info={"key":"value",
#       "Jim":34,
#       "Carry":69}

# val=info["lara"]
# print(val)

# # Exception Handling
# # try:   , except:    , else:    , finally:    

# try:
#     file=open("hello.txt")
#     info={"key":"value",
#       "Jim":34,
#       "Carry":69}
#     val=info["lara"]
# except FileNotFoundError:
#     file=open("new_file.txt","w")
# except KeyError:
#     print("This key does not exist")
# else:
#     content=file.read()
#     print(content)


# # raise - to raise our own excepts
# finally:
#     raise KeyError("Error created by pragrammer")

 
# BMI calculator
height=float(input("Enter height"))
weight=float(input("Enter weight"))

if height>3:
    raise ValueError ("Human height cannot be over 3 meters")



bmi= weight/height**2
print(bmi)

def hello(num):
    print(hello)

hello(4)



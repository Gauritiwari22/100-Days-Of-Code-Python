"Files, directories and Paths"

#opening a file

file=open("Day24/my_file.txt")

# Reading a file
contents=file.read()
print(contents)

file.close()

# Using with keyword
with open("Day24/my_file.txt") as file:
    contents=file.read()
    print(contents) #No need to mention to close the file now

# Writing inside a file
with open("Day24/my_file.txt",mode="a") as file:
    file.write("\nI am practicing coding for 100 days straight to brush up my coding skills.")
    print(contents)


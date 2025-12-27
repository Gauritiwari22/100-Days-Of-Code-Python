"Day4"

# Random module- random module is used, it is used to choose random numbers from a range of numbers
#using random.randint

import random
random_integer=random.randint(1,10)
print(random_integer)

#creating our own module- createdd another python fule and imported it as module to use it
import module
print(module.fav_color)
print(module.fav_fruit)

# for printing random floating poitn numbers
#randon.random() is used to create a random floating number between 0 and 1(0 is included 1 is not)
print(random.random())

#to print random float numbers between 0 and n( here 5)
random_num=random.random()*5
print(random_num)

print(random.uniform(1,20)) #1 and 20 both included


#using random module to print output of tossing a coin
toss=random.randint(0,1)
if toss==0:
    print("Heads")
else:
    print("Tails")


#lists- a data structure used for organising and storing data in []. Ordered and mutable.
fruits=["apple","banana","cherry"]
print(fruits[0]) #prints apple- first element
print(fruits[-1]) #prints cherry= last element
fruits[2]="watermelon" #ediiting element inside the list
print(fruits)

#append() function- adds element in the end, extend() function- adds multiple elements in the end
fruits.append("cherry")
fruits.extend(["pear","mango"])
print(fruits)

# choosing a random person to pay the bill from the list

names=["Gauri","Alex","Bob","Sumit","Priya","Alok"]
print(random.choice(names))

person=random.randint(0,4)
print(names[person])

# Nested lists- list inside another list
vegetables=["onion","carrot","capsicum","pumpkin","raddish"]
healthy_food=[fruits,vegetables]
print(healthy_food)



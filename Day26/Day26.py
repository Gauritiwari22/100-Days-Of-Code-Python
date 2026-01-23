"Day 26"

# List comprehension

nums=[1,2,3]
new_list=[]
for num in nums:
    new_num=num+1
    new_list.append(new_num)

print(new_list)

nums=[1,2,3]
new_list=[n+1 for n in nums]  # Using list comprehension
print(new_list)

# Examples

name="Gauri"
name_list=[letter for letter in name]
print(name_list)

numbers=range(1,5)
squared_nums=[i*2 for i in numbers]
print(squared_nums)

# Conditional list comprehension - a condition is added which needs to be satisfied

names=["Rajeev","Sushila","Priyanka","Kat","Bob","Alex","Aishwarya"]
new_names1=[x for x in names if len(x)<=4]
print(new_names1)
new_names2=[x.upper() for x in names if len(x)>=5]
print(new_names2)

# Dictionary comprehension

# syntax={new_key:new_value for item in list}
# syntax={new_key:new_value for (key,value) in dict.items() if ....}

import random
names=["Rajeev","Sushila","Priyanka","Kat","Bob","Alex","Aishwarya"]
student_scores={name:random.randint(1,100) for name in names}
print(student_scores)
passed_students={name:score for (name,score) in student_scores.items() if score>60} # with condition
print(passed_students)

# Iterating over Pandas DataFrame

student_dict={
    "name":["Alex","Bob","Charlie"],
    "marks":[56,89,67]
}

# Looping through dictionary

for key,value in student_dict.items():
    print(key)
    print(value)

import pandas as pd
df=pd.DataFrame(student_dict)
print(df)

# Looping through a data frame

for (index,row) in df.iterrows():
    print(row)
    print(row.name)
    print(row.marks)



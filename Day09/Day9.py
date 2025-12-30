"Day9"

# Dictionaries - stores data as key value pairs
# syntax = {key:value}

info={
    "name": "james",
    "place": "New York",
    "occupation": "student"
}

print(info)

# accessing values
print(info["name"])
print(info["place"])

# adding key-value pair
info["age"]=25
print(info)

# editting a value in a dictionary
info["age"]=29
print(info)  # updated dictionary printed

# Looping through a dictionary

for key in info:
    print(key)
    print(info[key])

# to print both together
for k,v in info.items():
    print(f"{k}:{v}")


for value in info.items():
    print(value)

# Student scores and grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
grade=""
for key in student_scores:
    if student_scores[key]>=91:
        grade="Outstanding"
    elif student_scores[key]>=81:
        grade="Exceeds expectations"
    elif student_scores[key]>=71:
        grade="Acceptable"
    else:
        grade="Fail"
    student_grades[key] = grade
print(student_grades)

# Nested list in dictionary
travel={
    "Haryana":["Hisar","Gurgaon","Kurukshetra"],
    "Maharashtra":["Pune","Mumbai","Nagpur"]
}

# Accessing items in the list inside the dictionary
print(travel["Haryana"][1])

# Nesting dictionary inside a dictionary
travel_log={
    "France": {
        "capital" : 'Paris',
        "places": ["Lille","Dijon"]
            },
    "Nepal": {
        "capital": "Kathmandu",
        "places": ["Pokhara","Lalitpur"]
    }

    }

# accessing 'Pokhara' from above nested dictionary
print(travel_log["Nepal"]["places"][0])
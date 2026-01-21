# # Working with CSV Data and Pandas librabry

# # Reading the csv file
# # import csv

# # with open("Day25/weather_data.csv") as csv_file:
# #     data=csv_file.readlines() # Not a very clean method of arranging our data
# #     print(data)
    
# #     data=csv.reader(csv_file) # more compact way
# #     temp=[]
# #     print(data)
# #     for row in data:
# #         print(row)

# #     for col in data: # to print the temperature column
# #         if col[1]!="temp":
# #             temp.append(int(col[1]))
# #     print(temp)


# # Pandas library - perform data analysis on tabular data

# import pandas as pd
# df=pd.read_csv("Day25/weather_data.csv")
# # print(type(df))
# # print(df)
# # print(df["temp"])

# # temp_list=df["temp"].to_list()
# # print(temp_list)

# # average_temp=(sum(temp_list))/len(temp_list)
# # print(average_temp)

# # # OR

# # print(df["temp"].mean())
# # print(df["temp"].max())

# # # Get data in row
# # print(df[df.day=="Monday"])
# # print(df[df.temp==df.temp.max()])

# # tuesday=df[df.day=="Tuesday"]
# # print(tuesday.condition)

# monday_temp=df[df.day=="Monday"]
# print(monday_temp)
# monday_temp.temp=(9/5*monday_temp.temp)+32
# print(monday_temp.temp)

# # Data frame from scratch

# data_dict={
#     "students":["Alice","Bob","Mary"],
#     "age":[19,23,19]
# }

# data_frame=pd.DataFrame(data_dict)
# print(data_frame)


import pandas as pd

squirrel_data=pd.read_csv("Day25/squirrel_data.csv")

gray_squirrels=len(squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels=len(squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(squirrel_data[squirrel_data["Primary Fur Color"]=="Black"])
print(gray_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

data_dict={
   "Fur Color":["Gray","Cinnamon","Black"],
   "Count":[gray_squirrels,
            cinnamon_squirrels,
            black_squirrels,]
}

count_of_colors=pd.DataFrame(data_dict)
print(count_of_colors)




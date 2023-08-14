# data = []
#
# with open("./weather_data.csv") as weather_data:
#     weather_data = weather_data.readlines()
#     for name in weather_data:
#         stripped_name = name.strip()
#         data.append(stripped_name)
#     print(data)


# import csv
#
# with open("./weather_data.csv") as weather_data:
#     weather_data = csv.reader(weather_data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# all_data = 0
# for no in data["temp"]:
#     all_data += no
#     average = all_data / len(data["temp"])
# print(average)
#
#
# ave = sum(data["temp"]) / len(data["temp"])
# print(ave)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# m_f = monday_temp * 9/5 + 32
# print(m_f)
#

# color = data["Primary Fur Color"]
# gray_count = 0
# red_count = 0
# black_count = 0
# for item in color:
#     if item == "Gray":
#         gray_count += 1
#     elif item == "Cinnamon":
#         red_count += 1
#     else:
#         black_count += 1

#OR
color = len(data["Primary Fur Color"])

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Data")




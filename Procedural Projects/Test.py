# # fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# # vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# # dirty_dozen = [fruits, vegetables]

# # #print(dirty_dozen)
# # print(dirty_dozen[0][1] + " " + dirty_dozen[1][0] )

# ######################
# # 🚨 Don't change the code below 👇
# row1 = ["️⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# #print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# horizonal = int(position[0])
# vertical = int(position[1])

# horizonal = horizonal - 1
# vertical = vertical - 1

# select_row = map[vertical]

# select_row[horizonal] = "X"







# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# num = 0
# for number in range(1, 101):
#     num = num + number
# print(num)

# name = ["may", "say", "hey"]

# nl = len(name)

# print(nl)

# travel_log = {
#     "France": {"Cites_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Nigeria": {"Cities_visited":["Lagos", "Abeokuta", "Ibadan", "Ekiti", "Ilorin", "Ilaro",]}
# }

class my_car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    def __str__(self):
        return f"{self.make,} {self.model}, {self.color}"

car = my_car("BMW", "M3", "Blue")

print(car.make)
print(car.model)
print(car.color)
print(car)
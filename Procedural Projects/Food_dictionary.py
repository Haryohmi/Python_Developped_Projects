food_log = [
{
  "Breakfast_Lunch_or_Dinner": "France",
  "visits": 12,
  "Food_options": ["Paris", "Lille", "Dijon"]
},
{
  "Breakfast_Lunch_or_Dinner": "Germany",
  "visits": 5,
  "Food_options": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_Breakfast_Lunch_or_Dinner(Breakfast_Lunch_or_Dinner , visits, Food_options):
    new_Breakfast_Lunch_or_Dinner = {}
    new_Breakfast_Lunch_or_Dinner["Breakfast_Lunch_or_Dinner"] = Breakfast_Lunch_or_Dinner
    new_Breakfast_Lunch_or_Dinner["visits"] = visits
    new_Breakfast_Lunch_or_Dinner["Food_options"] = Food_options
    food_log.append(new_Breakfast_Lunch_or_Dinner)

# add_new_Breakfast_Lunch_or_Dinner(Breakfast_Lunch_or_Dinner= Russia , visits= 2, Food_options=Moscow", "Saint Petersburg )
#🚨 Do not change the code below
add_new_Breakfast_Lunch_or_Dinner("Russia", 2, ["Moscow", "Saint Petersburg"])
print(food_log)

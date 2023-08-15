# LIST COMPREHENSION

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)
#
# range(1,5)
# new_range_list = [number*2 for number in range(1,5)]
# print(new_range_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# DICTIONARY COMPREHENSION

import random

students_scores = {student:random.randint(1, 100) for student in names}



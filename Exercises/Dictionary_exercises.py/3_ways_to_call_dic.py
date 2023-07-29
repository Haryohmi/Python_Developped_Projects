#These are the three ways to call a dictionary

"""important factors are the curly bracket, the key sting identifier,
the colon that seperates key and value, and the coma
at the end of each key and value"""

#1. Using curly bracket {}
#example
my_dictionary = {"key": "value",
                 "key2": "value2",
                 "key3": int_value}

#2. using dict()
my_dictionary = dict({"key": "value",
                 "key2": "value2",
                 "key3": int_value})
#3. sequencial pair
#my_dictionary = dict([("key": "value"), ( "key2": "value2")])

#Two ways to access dictionary

#1. 
print(my_dictionary["key2"])
#2.
print(my_dictionary.get("key3"))

#getting all keys and values
#key() Returns all keys in the dictionary
#value() Returns all values in the dictionary
#items() Returns all items (key-value pair) as a tuple in a dictionary

#iterating a dictionary
print("key", ":", "value")
for key in my_dictionary:
    print(key, ";", my_dictionary[key])

print("key", ":", "value")
for key_value in my_dictionary.items():
    print(key_value[0], key_value[1])


#adding items to the dictionary 
#example
my_dictionary["new_key"] = "new_value"
var = {
    "China": "143",
    "India": "136",
    "USA": "32",
    "Pakistan": "21"
}


def details(action, add=0, remove=0, query=0):
    var = {
        "China": "143",
        "India": "136",
        "USA": "32",
        "Pakistan": "21"
    }

    if action == "print":
        for key in var:
            print(f"{key}==>{var[key]}")
    elif action == "add":
        question2 = input("Enter country name: ")
        if question2 in var:
            print(f"{question2} already exists with population: {var[question2]}")
        else:
            population = input("Enter population: ")
            var[question2] = str(population)
        # Print the updated dictionary
        for key in var:
            print(f"{key}==>{var[key]}")
    elif action == "remove":
        country = input("Enter country: ")
        if country in var:
            del var[country]
            print(f"{country} removed.")
        else:
            print(f"{country} doesn't exist.")
        # Print the dictionary after removal
        for key in var:
            print(f"{key}==>{var[key]}")

    elif action == "query":
        country = input("Enter country: ")
        if country in var:
            print(f"{var[country]}")
        else:
            print(f"{country} doesn't exist.")

if __name__ == '__main__':
    action = input("Enter action (print/add/remove/query): ").strip().lower()
    details(action)
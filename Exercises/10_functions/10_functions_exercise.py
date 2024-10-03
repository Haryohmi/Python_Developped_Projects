def calculate_area(d1, d2, shape="triangle"):
    shape = input("what is the shape:")
    if shape == "rectangle":
        area = d1 * d2
    elif shape == "triangle":
        area = 1 / 2 * (d1 * d2)
    else:
        print("incorrect shape")
    print(f"Area of the {shape} is", area)


if __name__ == '__main__':
   d1 = int(input(f"Enter value for d1:"))
   d2 = int(input(f"Enter value for d2:"))
   calculate_area(d1, d2)


#Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

   def print_pattern(n):
    for i in range(1, n + 1):
        answer = ""
        for j in range(i):
            answer = answer + "*"
        print(answer)
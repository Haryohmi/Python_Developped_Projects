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
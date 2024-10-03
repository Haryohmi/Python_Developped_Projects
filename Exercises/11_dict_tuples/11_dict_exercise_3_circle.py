def circle_calc():
    radius = int(input("Enter the radius of the circle: "))
    pi = 3.14
    area = pi * (radius**2)
    circumference = 2 * pi * radius
    diameter = 2 * radius
    print(f"Area = {area}\nCircumference = {circumference}\nDiameter = {diameter}")



if __name__ == '__main__':
    circle_calc()
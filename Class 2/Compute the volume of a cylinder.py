

import math

def calculate_cylinder_properties(radius, length):
    area = math.pi * radius * radius
    volume = area * length
    return area, volume

def main():
    radius = float(input("Enter the radius of the cylinder: "))
    length = float(input("Enter the length of the cylinder: "))
    area, volume = calculate_cylinder_properties(radius, length)

    print(f"The area of the cylinder is: {area:.2f}")
    print(f"The volume of the cylinder is: {volume:.2f}")

if __name__ == "__main__":
    main()
69

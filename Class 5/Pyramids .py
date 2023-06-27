def display_pyramid(lines):
    for i in range(1, lines + 1):
        print(" " * (lines - i), end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()
while True:
    try:
        num_lines = int(input("Enter the number of lines (1-15): "))
        if 1 <= num_lines <= 15:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 15.")
    except ValueError:
        print("Invalid input. Please enter a number.")


display_pyramid(num_lines)

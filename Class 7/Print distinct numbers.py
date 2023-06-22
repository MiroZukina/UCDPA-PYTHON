def print_distinct_numbers():
    numbers = input("Enter numbers separated by a space: ").split()

    numbers = [int(num) for num in numbers]

    distinct_numbers = []

    for num in numbers:
        if num not in distinct_numbers:
            distinct_numbers.append(num)

   
    print("The distinct numbers are:", end=" ")
    for num in distinct_numbers:
        print(num, end=" ")
    print()

print_distinct_numbers()
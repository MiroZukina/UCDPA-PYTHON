def count_occurrences():
   
    occurrences = {}

    numbers = input("Enter a series of integers (between 1 and 100), separated by spaces: ").split()

    
    numbers = [int(num) for num in numbers]

    for num in numbers:
        if 1 <= num <= 100:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

    for num, count in occurrences.items():
        print("Number", num, "occurs", count, "times.")

count_occurrences()
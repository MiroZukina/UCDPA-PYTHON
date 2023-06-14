# task 1

print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is fun")
 

 # task 2 

for _ in range(5):
    print("Welcome to Python")


# Task 3 

display = "FUN"
print_F = [["" for i in range(5)] for j in range(6)]
print_U = [["" for i in range(5)] for j in range(7)]
print_N = [["" for i in range(5)] for j in range(8)]

# Code for F
lF = ""
for row in range(5):
    for col in range(6):
        if (col == 0 or col == 1) or ((row == 0 or row == 2) and (col < 5)):
            lF += "F"
        else:
            lF += " "
    lF += "\n"

# Code for U
lU = ""
for row in range(5):
    for col in range(7):
        if ((col == 0 or col == 6) and (row < 3)) or ((row == 3) and (col == 1 or col == 5)) or ((row == 4) and (col > 1 and col < 5)):
            lU += "U"
        else:
            lU += " "
    lU += "\n"

# Code for N
lN = ""
for row in range(6):
    for col in range(8):
        if (col == 0 or col == 1 or col == 6 or col == 7) or (row == col):
            lN += "N"
        else:
            lN += " "
    lN += "\n"

print(lF,lU,lN)

#task 5

a = 9.5 * 4.5 - 2,5 * 3 / 45.5 - 3.5
print(a)
import random
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

correct_sum = num1 + num2

user_sum = int(input(f"What is the sum of {num1} and {num2}? "))

is_correct = user_sum == correct_sum


print(f"Your answer is {is_correct}. The correct sum is {correct_sum}.")


def feet_to_meters(feet):
    meters = feet * 0.305
    return meters

feet = float(input("Enter a number in feet: "))

meters = feet_to_meters(feet)

print(f"{feet} feet is equal to {meters} meters.")

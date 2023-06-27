def kg_to_lb_pounds_to_kg():
    print("Kilograms\tPounds\t|\tPounds\tKilograms")
    print("---------------------------------------------")

    for kg in range(1, 200):
        lb = round(kg * 2.2, 2)
        kg_lb_conversion = round(lb * 0.45, 2)
        print(f"{kg}\t\t{lb}\t|\t{lb}\t\t{kg_lb_conversion}")

kg_to_lb_pounds_to_kg()

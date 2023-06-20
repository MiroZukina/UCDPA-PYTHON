# Prompt the user for employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax_withholding_rate = float(input("Enter federal tax withholding rate (in decimal): "))
state_tax_withholding_rate = float(input("Enter state tax withholding rate (in decimal): "))

# Calculate the gross pay
gross_pay = hours_worked * hourly_pay_rate

# Calculate the withholding amounts
federal_tax_withholding = gross_pay * federal_tax_withholding_rate
state_tax_withholding = gross_pay * (state_tax_withholding_rate)

# Calculate the net pay
net_pay = gross_pay - federal_tax_withholding - state_tax_withholding

# Print the payroll statement
print("Payroll Statement for", employee_name)
print("Hours Worked:", hours_worked)
print("Hourly Pay Rate: $", hourly_pay_rate)
print("Gross Pay: $", gross_pay)
print("Deductions:")
print("  Federal Tax Withholding (" + str(federal_tax_withholding_rate * 100) + "%): $", federal_tax_withholding)
print("  State Tax Withholding (" + str(state_tax_withholding_rate *100) + "%): $", state_tax_withholding)
print("Net Pay: $", net_pay)

#initialization of values for netIncome, grossIncome, nameOfEmployee, pagibigContribution
net_income = -0
gross_income = 0
total_deduction = 0
end_name = " "
pagIbig_contribution = 100.00

# getting the inputs for ratePerHour, numberOfHoursPerDay, numberOfDaysPerWeek, numberOFWeeksPerMonth, sssContribution, philhealthContribution
rate_per_hour = float(input("Enter the employee's rate per hour:"))
num_hrs_per_day = float(input("Enter the Employee's rate per day:"))
num_days_per_week = int(input("Enter the Employee's rate per week:"))
num_weeks_per_month = int(input("Enter the Employee's rate per month:"))
sss_contribution = float(input("Enter the Employee's rate of contribution:"))
philHealth_contribution = float(input("Enter the Employee's rate of contribution:"))
tax_contributions = float(input("Enter the Employee's rate of contribution:"))

# getting the formula for the computation for the grossIncome, totalDeduction, netIncome
gross_income = rate_per_hour * num_hrs_per_day * num_days_per_week * num_weeks_per_month * num_weeks_per_month
total_deduction = sss_contribution + philHealth_contribution + tax_contributions + pagIbig_contribution
net_income = gross_income - total_deduction

print("Employee Name:",nameEmployee)
print("Net Income:",net_income)
print("Gross Income:",gross_income)
print("Total Deduction:",total_deduction)

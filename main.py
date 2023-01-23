#Program Header
#Name: Rohan Oelofse
#Date: 01/23/2023
#GitHub URL: https://github.com/RohanOelofse/PythonProjects
#This program calculates annual salary based on hours.
#This calculator will calculate the unadjusted and adjusted annual salary.

DASH_LENGHT = 40
print("=" * DASH_LENGHT)
print("The Salary Calculator program")
print("=" * DASH_LENGHT)
COLUMN_LENGHT = 25
salary_per_hour = float(input(f"{'Salary per hour':.<{COLUMN_LENGHT}}: "))
hours_per_week = int(input(f"{'Hours per Week':.<{COLUMN_LENGHT}}: "))
days_per_week = int(input(f"{'Days per Week':.<{COLUMN_LENGHT}}: "))
holidays_per_year = int(input(f"{'Holidays per Year':.<{COLUMN_LENGHT}}: "))
vacation_days_per_year = int(input(f"{'Vacation Days per Year':.<{COLUMN_LENGHT}}: "))
working_days_per_year = 52 * days_per_week
hours_per_day = hours_per_week / days_per_week
unadjusted_salary = salary_per_hour * hours_per_day * working_days_per_year
adjusted_salary = salary_per_hour * hours_per_day * (working_days_per_year - holidays_per_year - vacation_days_per_year)
print(f"{'Unadjusted Salary':.<{COLUMN_LENGHT}}: ${unadjusted_salary:6,.2f}")
print(f"{'Adjusted Annual Salary':.<{COLUMN_LENGHT}}: ${unadjusted_salary:6,.2f}")
print("=" * DASH_LENGHT)
print("Goodbye!")

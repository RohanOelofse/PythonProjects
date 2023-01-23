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

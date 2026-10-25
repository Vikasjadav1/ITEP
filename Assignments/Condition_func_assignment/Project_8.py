'''
8. Employee Attendance and Salary Calculator
Intermediate
Concepts: Conditions, loops, functions, dictionaries
Requirements
•	Enter employee details and days present.
•	Calculate attendance percentage.
•	Calculate salary based on days worked.
•	Apply a bonus or deduction according to attendance rules.
•	Generate an employee summary.

'''


result={
    "Employee_Name":None,
    "id":id,
    "total_working_days":25,
    "present":24,
    "attendance_percentage": None,
    "earned_salary":None,
    "bonus/Deduction":None,
    "final_salary":None
}

def attendence_per(present_days,total_working_days):
    attendece=(present_days/total_working_days)*100
    return attendece

def salary_cal(present_days,total_working_days,salary):
    per_day_salary=salary/total_working_days
    earned_salary=per_day_salary*present_days
    return earned_salary

def bonus(attendence,earned_salary):
    if attendence>=95:
        bonus=1000
    elif attendence>=80 and attendence<95:
        bonus=0
    else:
       bonus=-500
    
    final_salary=earned_salary + bonus
    return final_salary, bonus

employees = []

num = int(input("Enter number of employees: "))

for i in range(num):
    print(f"\nEnter details of Employee {i + 1}")

    name = input("Enter name: ")
    emp_id = int(input("Enter employee ID: "))
    salary = float(input("Enter monthly salary: "))
    total_working_days = int(input("Enter total working days: "))
    present = int(input("Enter days present: "))

    if total_working_days <= 0 or present < 0 or present > total_working_days:
        print("Invalid working days or attendance!")
        continue

    attendance = attendence_per(present, total_working_days)
    earned_salary = salary_cal(present, total_working_days, salary)
    final_salary, bonus_amount = bonus(attendance, earned_salary)

    result = {
        "Employee_Name": name,
        "id": emp_id,
        "total_working_days": total_working_days,
        "present": present,
        "attendance_percentage": attendance,
        "earned_salary": earned_salary,
        "bonus/Deduction": bonus_amount,
        "final_salary": final_salary
    }

    employees.append(result)


print("\n===== Employee Salary Summaries =====")

for employee in employees:
    print("\n-------------------------")
    for key, value in employee.items():
        print(f"{key}: {value}")








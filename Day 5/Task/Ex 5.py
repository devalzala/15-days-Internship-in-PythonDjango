class Employee:
    name = "Devalsinh"
    designation = "Designing"

class EmployeeField(Employee):
    salary = 25000

emp = EmployeeField
print("Employee details are \nName: ",emp.name,"\nDesignation: ",emp.designation,"\nsalary: ",emp.salary)
# sorting using lambda function
employees = [
    {'Name': 'Papa', 'age': 52, 'salary': 100000},
    {'Name': 'Imrana', 'age': 46, 'salary': 99999},
    {'Name': 'Hassan', 'age': 21, 'salary':0},
    {'Name':'Hussain', 'age': 19, 'salary':0},
]

employees.sort(key = lambda x: x.get('Name'))
print(employees, end='\n\n')

employees.sort(key = lambda x: x.get('age'))
print(employees, end='\n\n')

employees.sort(key=lambda x: x.get('salary'))
print(employees, end='\n\n')



# sorting using custom key 
employees = [
    {'Name': 'Hasan', 'age': 21, 'salary': 70000},
    {'Name': 'Surabhi', 'age': 20, 'salary': 80000},
    {'Name': 'Hussain', 'age': 19, 'salary': 90000},
]

def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')


employees.sort(key=get_name)
print(employees, end='\n\n')

employees.sort(key=get_age)
print(employees, end='\n\n')

employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')
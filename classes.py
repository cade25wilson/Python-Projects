class Person:
    #Attributes for people who are involved in a school
    name = ''
    id_number = ''
    password = 'Schoolsecurity0915'
    age = ''
    
class Student(Person):
    grade_level = ''
    major = ''

class Employee(Person):
    pay_rate = '15.00'
    weekly_schedule = 'Mon, Thur, Fri'
    job = 'janitor'

class Person:
    #Attributes for people who are involved in a school
    name = 'Tom'
    id_number = '1399822'
    password = 'Schoolsecurity0915'
    age = '24'

    def selfIntro(Self):
        self_name = input("Enter your name: ")
        self_age= input("enter your age: ")
        print("My name is {}, and I am a {} year old at this school".format(self_name, self_age))
    
class Student(Person):
    grade_level = 'Freshman'
    major = 'psychology'

    def selfIntro(Self):
        self_name = input("Enter your name: ")
        self_major= input("enter your major: ")
        print("My name is {}, and I am a {} Major at this school".format(self_name, self_major))
    

class Employee(Person):
    pay_rate = '15.00'
    weekly_schedule = 'Mon, Thur, Fri'
    job = 'janitor'

    def selfIntro(Self):
        self_name = input("Enter your name: ")
        self_job= input("enter your job: ")
        print("My name is {}, and I am a {} at this school".format(self_name, self_job))
    


    
prospect = Person()
prospect.selfIntro()

scholar = Student()
scholar.selfIntro()

laborer = Employee()
laborer.selfIntro()


class Person:
    #Attributes for people who are involved in a school
    name = ''
    id_number = ''
    password = ''
    age = ''

    def selfIntro(Self):
        self_name = input("Enter your name: ")
        self_age= input("enter your age: ")
        print("My name is {}, and I am a {} year old at this school".format(self_name, self_age))
    
class Student(Person):
    grade_level = ''
    major = ''

    def selfIntro(Self):
        self_name = input("Enter your name: ")
        self_major= input("enter your major: ")
        print("My name is {}, and I am a {} Major at this school".format(self_name, self_major))
    

class Employee(Person):
    pay_rate = ''
    weekly_schedule = ''
    job = ''

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


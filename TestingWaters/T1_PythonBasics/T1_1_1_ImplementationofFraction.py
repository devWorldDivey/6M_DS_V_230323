class Fraction:
    def __init__(self,n,d) -> None:
        self.n = n
        self.d = d
    def __str__(self) -> str:
        return "{}/{}".format(self.n,self.d)
# Reference variable
    # Pass by reference
    
class Customer:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello",customer.name,"sir")
    if customer.gender == "Female":
        print("Hello",customer.name,"ma'am")
cust = Customer("Ankita","Female")
greet(cust)

# Inheritance

class  User:
    def login(self):
        print("Login")
    def register(self):
        print("Register")
        
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

stu1 = Student()
stu1.enroll()
stu1.login()
stu1.register()
stu1.review()

u = User()
u.login()
u.register
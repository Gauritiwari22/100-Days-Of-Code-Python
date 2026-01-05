class Book:

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def display_info(self):
        print(
            f"The book title is {self.title}, "
            f"the author is {self.author}, "
            f"and the book has {self.pages} pages."
        )

book1=Book("The Palace of Illusions","Chitra Banerjee","312")
book2=Book("Student Stories","Ruskin Bond","200")

book1.display_info()
book2.display_info()




class BankAccount:

    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        
        if self.balance>=amount:
            self.balance-=amount
            print("Money withdrawn")
        else:
            print("Insufficient balance")


transactions=BankAccount(12000)
transactions.deposit(3000)
transactions.withdraw(4000)
print(f"Final Balance: {transactions.balance}")


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def compare(self,other_student):
        if self.marks>other_student.marks:
            print(f"{self.name} scored more marks than {other_student.name}.")
        elif self.marks<other_student.marks:
            print(f"{other_student.name} scored more marks than {self.name}.")
        elif self.marks==other_student.marks:
            print(f"{other_student.name} and {self.name} scored equal marks.")
        
student_1=Student("Ravi",56)
student_2=Student("Sonia",98)
student_1.compare(student_2)



class College:
    college_name="IGDTUW"

    def __init__(self,name,branch):
        self.name=name
        self.branch=branch

    def display_details(self):
        print(
            f"Student name: {self.name}, "
            f"Student college: {College.college_name}, "
            f"student branch: {self.branch}"
            )
        
Student1=College("Preeta","CSE")
Student2=College("Saanvi","MAE")

Student1.display_details()
Student2.display_details()


        
        





    
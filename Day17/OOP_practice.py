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



class QuizQuestion:

    def __init__(self,question,correct_answer):
        self.question=question
        self.correct_answer=correct_answer

    def check_answer(self,user_answer):
        if self.correct_answer==user_answer:
            print("Correct!")
            return True
        else:
            print("Wrong!")
            return False
class Quiz:
    def __init__(self):
        self.score=0
    def update_score(self,result):
        if result==True:
            self.score+=1
    def show_score(self):
        print(f"Your score is {self.score}")

            

quiz=Quiz()


question_1=QuizQuestion("Python language has a very readable and beginner-friendly syntax.(True/False): ","true")
question_2=QuizQuestion("Python is named after the snake Python.(True/False): ","false")


print(question_1.question)
result=question_1.check_answer(input("Enter answer: "))
quiz.update_score(result)
quiz.show_score()
print(question_2.question)
result=question_2.check_answer(input("Enter answer: "))
quiz.update_score(result)
quiz.show_score()



class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
    def decrement(self):
        self.count-=1
        if self.count<0:
            self.count=0
    def show_count(self):
        print(f"Current count: {self.count}")

count=Counter()
count.increment()
count.decrement()
count.decrement()
count.decrement()
count.show_count()


class User:
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self,input_username,input_password):
        if self.username==input_username and self.password==input_password:
            print("Login successful!")
        else:
            print("Invalid credentials.")

user1 = User("alex123", "KHF123bgh")
user2 = User("sonia45", "pass@123")

user1.login(input("Enter username: "),input("Enter password: "))
user2.login(input("Enter username: "),input("Enter password: "))
        


class Product:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def compare_price(self,other_product):
        if self.price>other_product.price:
            print(f"{other_product.name} are cheaper than {self.name}.")
        elif self.price<other_product.price:
            print(f"{self.name} are cheaper than {other_product.name}.")
        else:
            print(f"{self.name} and {other_product.name} are equal in cost.")
        
product_1=Product("Onions",45)
product_2=Product("Tomatoes",99)
product_1.compare_price(product_2)



class Result:

    def __init__(self,name,marks_list):
        self.name=name
        self.marks_list=marks_list

    def calculate_average(self):
        summation=sum(self.marks_list)
        average=summation/len(self.marks_list)
        return average

    def check_pass_fail(self):
        average=self.calculate_average()
        if average>=40:
            print("Pass")
        else:
            print("Fail")

student_1=Result("Aanya",[56,73,92,91,28])
student_2=Result("Sumit",[63,82,16,83,14])

student_1.check_pass_fail()
student_2.check_pass_fail()









    
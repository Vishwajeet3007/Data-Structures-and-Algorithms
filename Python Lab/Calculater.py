#Write a program in python to Add/Sub/Divide/Multiply Using Dot format 
class Calculator:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def sub(x,y):
        return x-y
    @staticmethod
    def multiply(x,y):
        return x*y
    @staticmethod
    def divide(x,y):
        if y==0:
            return "Cannot divide by Zero(0)."
        return x/y
    

calc = Calculator()

    #Addition
result_add = calc.add(5,3)
print("Addition : ", result_add)

#Subtraction
result_sub = calc.sub(5,3)
print("Subtraction: ", result_sub)

#Multiplication
result_multiply = calc.multiply(5,4)
print("Multiplication : ", result_multiply)

#Division
result_divide= calc.divide(8,2)
print("division: ",result_divide)

        
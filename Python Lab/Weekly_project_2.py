def add(a,b):
    return a + b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Error! , Division is Zero."
    return a / b
def calculator():
    print("Simple Calculator")
    print("Select Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        nums1=float(input("Enter first number: "))
        nums2=float(input("Enter second number: "))
        if choice == '1':
            print("Result : ",add(nums1,nums2))
        elif choice == '2':
            print("Result : ",sub(nums1,nums2))
        elif choice == '3':
            print("Result : ",mul(nums1,nums2))
        elif choice == '4':
            print("Result : ",div(nums1,nums2))
    else:
        print("Invalid Input")
if __name__=="__main__":
    
    calculator()

    
    
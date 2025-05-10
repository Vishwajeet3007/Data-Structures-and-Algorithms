# fibonacci series without using third variable
def fib(n):
  a=0
  b=1
  
  for _ in range(n):
      print(a , end=" ")
      a = a ^ b
      b = a ^ b
      a = a ^ b
      b=a+b
  
  # Input: number of terms
n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {n} terms:")
    fib(n)
    
    
    

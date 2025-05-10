#write a program in python to Segregate even and odd numbers 
def segregate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = segregate_even_odd(numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)

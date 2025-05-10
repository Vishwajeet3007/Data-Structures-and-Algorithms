def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    compound_interest = amount - principal
    return compound_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time (in years): "))

    si = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: {si}")

    n = int(input("Enter the number of times interest is compounded per year: "))

    ci = calculate_compound_interest(principal, rate, time, n)
    print(f"Compound Interest: {ci}")

if __name__ == "__main__":
    main()

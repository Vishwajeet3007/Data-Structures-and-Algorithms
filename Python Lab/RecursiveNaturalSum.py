row = int(input("Enter the number:"))
num = ord('A')  # Get the ASCII value of 'A'
for i in range(1, row + 1):
    for j in range(i):
        print(chr(num), end=" ")  # Convert ASCII value to character
        if num == ord('A'):  # Change to 'B' when 'A' is encountered
            num = ord('B')
        else:
            num += 1
    print()
number = input("Enter a number, I'll tell u if it's multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is multiple of ten")
else:
    print(f"The number {number} isn't multiple of ten")

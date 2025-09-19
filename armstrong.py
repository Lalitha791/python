def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

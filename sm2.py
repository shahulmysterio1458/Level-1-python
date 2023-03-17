def is_armstrong_number(num):
    """Returns True if the given number is an Armstrong number, False otherwise."""
    
    digit_sum = sum([int(digit)**3 for digit in str(num)])
    return digit_sum == num

N = int(input("Enter the size of the list: "))
values = []
for i in range(N):
    values.append(int(input(f"Enter value {i+1}: ")))

for i in range(N):
    if is_armstrong_number(values[i]):
        values[i] = 1
    else:
        values[i] = 0


print("Updated list: ", values)

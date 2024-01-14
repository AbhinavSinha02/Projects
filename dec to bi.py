#Pythion code to convert decimal number to binary and vice versa
def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Negative numbers are not supported"
    elif decimal_number == 0:
        return "0b0"
    else:
        binary_representation = bin(decimal_number)
        return binary_representation

# Get user input
decimal_input = int(input("Enter a decimal number: "))

# Convert to binary and display the result
binary_result = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_result}")

#Binary to decimal code

def binary_to_decimal(binary_number):
    try:
        decimal_representation = int(binary_number, 2)
        return decimal_representation
    except ValueError:
        return "Invalid binary number"

# Get user input
binary_input = input("Enter a binary number: ")

# Convert to decimal and display the result
decimal_result = binary_to_decimal(binary_input)
print(f"The decimal representation of {binary_input} is: {decimal_result}")

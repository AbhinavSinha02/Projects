#convert binary number to hexadecimal
def binary_to_hexadecimal(binary_number):
    try:
        decimal_representation = int(binary_number, 2)
        hexadecimal_representation = hex(decimal_representation)
        return hexadecimal_representation
    except ValueError:
        return "Invalid binary number"

# Get user input
binary_input = input("Enter a binary number: ")

# Convert to hexadecimal and display the result
hexadecimal_result = binary_to_hexadecimal(binary_input)
print(f"The hexadecimal representation of {binary_input} is: {hexadecimal_result}")

#convert hexadecimal number to binary

def hexadecimal_to_binary(hexadecimal_number):
    try:
        decimal_representation = int(hexadecimal_number, 16)
        binary_representation = bin(decimal_representation)
        return binary_representation
    except ValueError:
        return "Invalid hexadecimal number"

# Get user input
hexadecimal_input = input("Enter a hexadecimal number: ")

# Convert to binary and display the result
binary_result = hexadecimal_to_binary(hexadecimal_input)
print(f"The binary representation of {hexadecimal_input} is: {binary_result}")





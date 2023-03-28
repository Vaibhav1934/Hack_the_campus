string = input("Enter a string: ")
hex_string = ""

for char in string:
    hex_val = hex(ord(char))[2:]  # convert character to its hexadecimal value
    hex_string += hex_val.zfill(2)  # add leading zeros if necessary

print(f"Hexadecimal representation of '{string}': {hex_string}")
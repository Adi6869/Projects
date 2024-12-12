
def caesar_cipher(shift, plaintext):
    result = ""
    for char in plaintext:
        if char.isalpha():
            ascii_conversion = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_conversion + shift) % 26 + ascii_conversion)
            result += shifted_char
        else:
            result += char
    
    return(result)
    

def caesar_decipher(shift, ciphertext):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_conversion = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_conversion - shift) % 26 + ascii_conversion)
            result += shifted_char
        else:
            result += char
    return result
            
print("Welcome to the Simple Caesar Cipher Encryption/Decryption Tool.")
plaintext = input("Enter the Text to be Encrypted/Decrypted: ")
choice_options = {1: "Encryption", 2: "Decryption"}
print("Select an option:")
for key, value in choice_options.items():
    print(f"{key}: {value}")

while True:
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice not in choice_options:
            print("Invalid choice, please select 1 for Encryption or 2 for Decryption.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer (1 or 2).")

while True:
    try:
        shift = int(input("Enter the shift value: "))
        break
    except ValueError:
        print("Please enter a valid Integer Input.")
if choice == 1:
    encrypted_text = caesar_cipher(shift, plaintext)
    print(f"Encrypted text = {encrypted_text}")
elif choice == 2:
    decrypted_text = caesar_decipher(shift, plaintext)
    print(f"Decrypted text = {decrypted_text}")
 
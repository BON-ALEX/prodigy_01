def caesar_cipher(text, shift, mode='encrypt'):
   
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Iterate over each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            result += char
    
    return result

def main():
    # Get user input
    text = input("Enter the message you want to encrypt or decrypt: ")
    shift = int(input("Enter the shift value(number): "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()
    
    # Validate mode
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return
    
    # Perform encryption or decryption
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

    if __name__ == "__main__":
        main()

https://www.linkedin.com/feed/update/urn:li:activity:7311107683082731522/

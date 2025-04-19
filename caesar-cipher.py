import random
alphabet = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
]

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                            
              88           
""")

# Function that takes 3 parameters and ciphers the text.
def caesar(original_text, shift_amount, encode_decode):
    output_cipher = ""
    cipher_option = ""
    alphabet_upper_or_lower = 0
    
    # Loop for every character in the given text. 
    for letter in original_text:
        # Check for non alphabet characters such as spaces, dashes, underscores, etc.
        if (letter not in alphabet[0]) and (letter not in alphabet[1]):
            output_cipher += letter
            continue
        else:
            # Determine which list the letter is in.
            if letter in alphabet[0]:
                alphabet_upper_or_lower = 0
            elif letter in alphabet[1]:
                alphabet_upper_or_lower = 1
            
            # Find the current index of the character in the respective alphabet list.
            current_position = alphabet[alphabet_upper_or_lower].index(letter)

            # Calculate shift based on cipher requirement. 
            if encode_decode == 1: # If encode[1] is selected.
                cipher_option = "encoded"
                new_position = (current_position + shift_amount) % 26
            elif encode_decode == 2: # If decode[2] is selected.
                cipher_option = "decoded"
                new_position = (current_position - shift_amount) % 26

            # Update the 'output_cipher' string with the character at the newly calculated position.
            output_cipher += alphabet[alphabet_upper_or_lower][new_position]
    
    # Send the 'output_text' and 'cipher_option' once the loop is complete.
    return output_cipher, cipher_option


again = True # Variable to keep the loop going.

# Continue prompting the user until they select No[2].
while again:
    cipher = int(input("\n\nWould you like to encode[1] or decode[2]? ")) # Prompt the user if they want to encode or decode.
    text = input("\nType your message: ") # Prompt the user for a message to cipher.
    shift = int(input("\nSelect the shift amount: ")) # Prompt user for the amount of characters they would like to shift.

    result, cipher_option = caesar(encode_decode=cipher, original_text=text, shift_amount=shift) # Calls the 'caesar' function.
    print(f"\nYour {cipher_option} text is: '{result}'")

    keep_going = int(input("\nWould you like to continue (Yes[1] or No[2])? ")) # Prompts user if they would like to cipher again.
    
    # Program stops if user says no[2] and prints a departing message.
    if keep_going == 2:
        again = False
        print("\nGoodbye!")

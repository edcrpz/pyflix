# import time
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
#
# def encrypt(text_param, shift_param):
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by
#     #  the shift amount and print the encrypted text.
#     # e.g.
#     # plain_text = "hello"
#     # shift = 5
#     # cipher_text = "mjqqt"
#     # print output: "The encoded text is mjqqt"
#
#     # HINT: How do you get the index of an item in a list:
#     # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#     cipher_text = ''
#     for i in range(len(text_param)):
#         new_index = alphabet.index(text_param[i]) + shift_param    # need new index to point new letter
#         # <list>.index("data in list") --> returns index number
#         cipher_text += alphabet[new_index]
#
#     print(f"Encoded text: {cipher_text}")
#
#
# def decrypt(text_param, shift_param):
#     # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the
#     # shift amount and print the decrypted text.
#     # e.g.
#     # cipher_text = "mjqqt"
#     # shift = 5
#     # plain_text = "hello"
#     # print output: "The decoded text is hello"
#     decipher_text = ''
#     for i in range(len(text_param)):
#         new_index = alphabet.index(text_param[i]) - shift_param  # need new index to point new letter
#         # <list>.index("data in list") --> returns index number
#         decipher_text += alphabet[new_index]
#
#     print(f"Decoded text: {decipher_text}")
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the
# # correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#
# print("\nProcessing...\n\n")
# time.sleep(2)
#
# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)
# else:
#     print("You chose an invalid direction")



# ============================== Challenge - make caesar() -- combine encrypt() and decrypt() ==============================
# ============================== Challenge - make caesar() -- combine encrypt() and decrypt() ==============================

import time
import cipherart


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# need to double alphabets, if z needs to shift, index will be out of range

print(cipherart.logo)


def caesar(direction_param, text_param, shift_param):
    output = ''
    if direction_param == 'decode':  # this should not be inside 'for' as it will be negative,
        shift_param *= -1  # and then positive, and negative again as 'for' loops

    for i in range(len(text_param)):
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if text_param[i] not in alphabet:  # checks if character in message is in alphabet
            output += text_param[i]  # if NOT, just append the letter to the output
        else:
            new_index = alphabet.index(text_param[i]) + shift_param  # Else, char is in alphabet and need to shift
            output += alphabet[new_index]

    print(f"The {direction_param}d result is: {output}")


use_program = True

while use_program:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26    # 28 % 26 (no. of letters in alphabet) returns 2

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    print("\nProcessing...\n\n")
    time.sleep(1)
    caesar(direction, text, shift)

    choice = input("\nDo you want to continue using the Cipher program? (yes/no)\n").lower()
    if choice == 'yes':
        use_program = True
    else:
        use_program = False
        print("\nThanks for using the program.\nGood bye!")


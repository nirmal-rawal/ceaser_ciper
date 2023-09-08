# Implementing the welcome() function 


def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

welcome()


#  Implementing the encrypt() function 


def encrypt(message, shift):
        encrypted_message = ""
        for letter in message:
            if letter.isalpha():
                letter = letter.upper()
                encrypted_letter = chr((ord(letter) - 65 + shift) %26 + 65)
                encrypted_message+=encrypted_letter
            else:
                encrypted_message+=letter
        return encrypted_message



#  – Implementing the decrypt() function 


def decrypt(message, shift):
                decrypted_message = ""
                for letter in message:
                    letter = letter.upper()
                    if letter.isalpha():
                        decrypted_letter = chr((ord(letter) - 65 - shift) %26 + 65)
                        decrypted_message+=decrypted_letter
                    else:
                        decrypted_message+=letter
                return decrypted_message




# Implementing the enter_message() function


    
def shift_length():
        while True:
            shift_number = int(input("What is the shift number:"))
            if shift_number>=1 and shift_number<=20:
                return shift_number
            else:
                print("Invalid shift length, try again!")
                continue

def message_or_file():
        user_type = input('Would you like to read from a file (f) or the console (c)?: ')
        return user_type
    
def is_file():
         while True:
              file_name = input("Enter the file name or location:")
              try:
                   with open(f"{file_name}", "r") as new_file:
                        read_file = new_file.readline()
                        return read_file
              except FileNotFoundError:
                   print("File not found!")
                   continue
              
def write_message(result):
         with open("results.txt", "w") as text_file:
          written_file = text_file.write("".join(result))
          return written_file
         
def program_continue():
        while True:
                user_input = input("Would you like to encrypt or decrypt another message? (y/n):")
                if user_input == "y":
                    main()
                elif user_input == "n":
                    print("Thank you for using the program! Goodbye!")
                    exit()
                else:
                    print("Invalid option, try again!")
                    continue

  
def main():

    while True:
         user_mode = input("Would you like to encrypt (e) or decrypt (d):")






        

         
#   file handling(input/output)


         if user_mode == "e":
              while True:
                  user_choice = message_or_file()
                  if user_choice == "f":
                      read_message = is_file()
                      shift_number = shift_length()
                      encrypted_result = f"{encrypt(read_message, shift_number)}"
                      write_message(encrypted_result)
                      print(encrypted_result)
                      break
                  elif user_choice == "c":
                      read_message = input("What message would you like to encrypt?:")
                      shift_number = shift_length()
                      encrypted_result = f"{encrypt(read_message, shift_number)}"
                      write_message(encrypted_result)
                      print(encrypted_result)
                      break
                  else:
                   print("Invalid choice, try again!")
                   continue
         elif user_mode == "d":
              while True:
                  user_choice = message_or_file()
                  if user_choice == "f":
                      read_message = is_file()
                      shift_number = shift_length()
                      decrypted_result = f"{decrypt(read_message, shift_number)}"
                      write_message(decrypted_result)
                      print(decrypted_result)
                      break
                  elif user_choice == "c":
                      read_message = input("What message would you like to encrypt?:")
                      shift_number = shift_length()
                      decrypted_result = f"{decrypt(read_message, shift_number)}"
                      write_message(decrypted_result)
                      print(decrypted_result)
                      break
                  else:
                   continue
         else:
             print("Invalid mode, try again!")
             continue
         program_continue()
main()
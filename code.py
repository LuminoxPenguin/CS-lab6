#Zackary Terry

#Encoder:
def encode(password):
    encoded_password_list = []
    encoded_password_string = ""
    
    for character in password:
        encoded_password_list.append(int(character) + 3)
    
    for item in encoded_password_list:
        encoded_password_string += str(item % 10)

    return encoded_password_string
    
#Decode (Callum)     
def decode_password(encoded_password):
    password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)
        password += shifted_digit
    return password

if __name__ == "__main__":
    Inputted_Password = False
    while True:
        #Menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        choice = input("Please enter an option: ")

        #Encode Option
        if choice == "1":
            decoded_password = input("Please enter your password to encode: ")
            encoded_password = encode(decoded_password)
            print("Your password has been encoded and stored!", end = "\n\n")
            Inputted_Password = True
        #Decode Option
        elif choice == "2":
            if Inputted_Password:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            else:
                print("Please encode a password before you decode")
        #Quit Option
        elif choice == "3":
            break
        #If any number between 1 and 3 is not entered
        else:
            "Please choose a number between 1 and 3"

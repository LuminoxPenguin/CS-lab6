#Zackary Terry

#Encoder:
def encode(password):
    encoded_password_list = []
    encoded_password_string = ""
    for character in password:
        #Encoding Process
        encoded_password_list.append(int(character) + 3)
    for item in encoded_password_list:
        #Subtracts 10 if number is 2 digits
        if item > 9:
            encoded_password_string += str(item-10)
        else:
            encoded_password_string += str(item)
    return encoded_password_string
    

if __name__ == "__main__":
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
        #Decode Option
        elif choice == "2":
            print("In Progress")
        #Quit Option
        elif choice == "3":
            break
        #If any number between 1 and 3 is not entered
        else:
            "Please choose a number between 1 and 3"

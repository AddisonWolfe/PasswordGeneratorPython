import sys
import random
import string


PASS_LEN = 0
PASS_COMPLEXITY = 1
NUMBER_OF_PASSWORDS = 2
#Program introduction
def usage():
    print("Welcome to Random Password Generator\n")
    print("Developed by Addison Wolfe, 7/12/2025\n")
    print("Github: AddisonWolfe\n")
    print("LinkedIn: AddisonWolfe\n")
    

def get_fields():
    

    while True:
        len = input("How long would you like each password to be?\n")
        try:
            len = int(len)
            if(len ==0):
                sys.exit(0)
            else:
                break
        except ValueError:
            print("Please enter a valid integer or 0 to exit")

    while True: 
        print("1. Letters\n")
        print("2. Letters and Numbers\n")
        print("3. Letters, Numbers, and Symbols\n")
        complexity = input("Which level of complexity would you like to use?\n")

        try:
            complexity = int(complexity)
            if(complexity <0 or complexity>3):
                print("Please choose a valid option or 0 to terminate")
            elif (complexity ==0):
                sys.exit(0)
            else:
                break
        except ValueError:
            print("Please choose a valid option or 0 to terminate")


    while True:
        num_generate = input("How many would you like to generate?\n")

        try:
            num_generate = int(num_generate)
            if(num_generate ==0):
                sys.exit(0)
            else:
                break
        except ValueError:
            print("Please enter a valid integer or 0 to terminate")

    return len, complexity, num_generate

def generate_passwords(data):

    pass_dict = {}

    for i in range(data[NUMBER_OF_PASSWORDS]):
        new_password = ""
        match data[PASS_COMPLEXITY]:

            #only letters
            case 1:
                for j in range(data[PASS_LEN]):
                    new_password = new_password + random.choice(string.ascii_letters)
                pass_dict[i +1] = new_password

            case 2:
                for j in range(data[PASS_LEN]):
                    match random.randint(0,1):
                        case 0:
                            new_password = new_password + str(random.randint(0,9))
                        case 1:
                            new_password = new_password + random.choice(string.ascii_letters)
                pass_dict[i+1] = new_password

            case 3:
                for j in range(data[PASS_LEN]):
                    match random.randint(0,2):
                        case 0:
                            new_password = new_password + str(random.randint(0,9))
                        case 1:
                            new_password = new_password + random.choice(string.ascii_letters)
                        case 2:
                            new_password = new_password + random.choice(string.punctuation)
                pass_dict[i+1] = new_password
    return pass_dict

def main():
    usage()

    user_data = get_fields()

    pass_dict = generate_passwords(user_data)

    print("Here is your password book:\n")
    for key,value in pass_dict.items():
        print(f"{key}: {value}")            

        
    return
main()
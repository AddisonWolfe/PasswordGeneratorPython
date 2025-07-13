import userEntry
import sys

def main():
    usage()

    user_data = userEntry(get_fields())

    return




#Program introduction
def usage():
    print("Welcome to Random Password Generator\n")
    print("Developed by Addison Wolfe, 7/12/2025\n")
    print("Github: AddisonWolfe\n")
    print("LinkedIn: AddisonWolfe\n")
    

def get_fields():
    len = "s"
    complexity = "s"
    num_generate = "s"


    while type(len) != int:
        len = input("How long would you like each password to be?\n")
        if(len == 0):
            sys.exit(0)
        elif(type(len) != int):
            print("Please enter a valid integer or 0 to terminate\n")

    while(type(complexity != int)): 
        print("1. Letters\n")
        print("2. Letters and Numbers\n")
        print("3. Letters, Numbers, and Symbols\n")
        complexity = input("Which level of complexity would you like to use?\n")

        if(complexity == 0):
            sys.exit(0)
        elif(type(complexity) != int):
            print("Please enter a valid integer or 0 to terminate\n")


    while type(num_generate) != int:
        len = input("How many would you like to generate?\n")
        if(num_generate == 0):
            sys.exit(0)
        elif(type(num_generate) != int):
            print("Please enter a valid integer or 0 to terminate\n")
        
    return len, complexity, num_generate

main()
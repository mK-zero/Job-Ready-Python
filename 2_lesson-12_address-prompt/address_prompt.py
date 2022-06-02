# Name: Firstname lastnam
# Date created: Current date
# Purpose: Code-along for Python course

user_address = input("Enter an address (e.g., 123 Main Street): ")
if user_address.strip(): # check that string is not empty (after removing leading and trailing spaces)
    print("Your address is " + user_address + ".")
    split_address = user_address.split()
    #print(split_address) # temporary instruction to verify the list
    print("Your house number is " + split_address[0] + ".")
    print("Your street is " + " ".join(split_address[1:]) + ".")

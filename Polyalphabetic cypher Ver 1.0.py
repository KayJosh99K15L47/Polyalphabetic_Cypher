
#Polyalphabetic cypher
#Converts message to a cypher text using a keyword instead of a shift number

#Version 1.0 - 

#Constants
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#Inputs
#Shift word 
shift_word = input("Input a shift word ").lower().strip()

message = input("Input a message to encode ").lower().strip()


#Main function
def main():
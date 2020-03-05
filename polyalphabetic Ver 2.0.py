
#Polyalphabetic cypher
#Converts message to a cypher text using a keyword instead of a shift number

#Version 2.0 - finding locations, building lists of numbers for shift_word and message

#Constants
ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#Main function
def main():
    
    #Inputs
    #Shift word 
    shift_word = input("Input a shift word ").lower().strip()
    #Message to encrypt
    message = input("Input a message to encode ").lower().strip()    
    
    #List for shift word 
    shift_ints = []    
    
    #finds the locations of letters in shift_word in ALPHABET
    for shift_letter in shift_word:
        for alpha in ALPHABET:
            if alpha == shift_letter:
                shifting_location = ALPHABET.index(shift_letter)
                shift_ints.append(shifting_location)
                #Test
                print(shifting_location)                

    #Finds the location of letters in message in ALPHABET
    for letter in message:
        for alpha in ALPHABET:
            if alpha == letter:
                location = ALPHABET.index(alpha)
                #Test
                print(location)
                    
    #Test
    print(shift_ints)
        
                
main()
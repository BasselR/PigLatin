#Takes input string

def piggifyWord(words):
    # Splits input into list of individual words
    words = words.split()
    # Creates the string where we will store our output
    pigLatin = "" 
    # For each word, create a new string
    for i in words: 
        # With first character at the end, + ay for pig latin
        # If it's the first word of the list, capitalize it
        if i == 0:
            pigLatinWord = words[i][1:].capitalize() + words[i][0].lower() + "ay"
            
        else:
            pigLatinWord = words[i][1:] + words[i][0].lower() + "ay"
        # Appends each new word to final output string
        pigLatin += (" " + pigLatinWord)
        
    print (pigLatin)
    
piggifyWord("Look at that girl in the red sweater")

#Takes input string

def piggifyWord(words):
    
    words = words.split()   #Splits input into list of individual words
    pigLatin = ""   #Creates the string where we will store our output
    
    for i in words:     #For each word, create a new string 
                                    #With first character at the end, + ay for pig latin
        if i == 0:                  #If it's the first word of the list, capitalize it
            pigLatinWord = words[i][1:].capitalize() + words[i][0].lower() + "ay"
            
        else:
            pigLatinWord = words[i][1:] + words[i][0].lower() + "ay"
            
        pigLatin += (" " + pigLatinWord)    #Appends each new word to final output string
        
    print (pigLatin)    #Print output pig latin
    
piggifyWord("Look at that girl in the red sweater") #Call pig latin function
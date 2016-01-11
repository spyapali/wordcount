# put your code here.

def read_in_file(filename):
    """ reads in a text file and tabulates the word count via a dictionary. """

    text_dic = {}


    the_file = open(filename)
    for line in the_file:
        line = line.strip() #removes whitespace 
        test_line = line.split(" ") 
        for word in test_line:
            word = word.lower() 
            if word in text_dic:    #if word in line of text, add it to our dictionary.
                text_dic[word] += 1 #increment by one each time word appears in each line.
            else:
                text_dic[word] = 1 #if it's not in the dictionary, then add it to the dictionary.

                
        
           



    return text_dic 

def print_dictionary(dictionary):
    """Prints the word and its frequency in our text file"""
    for key_value in dictionary.iteritems():
        print "%s %d" %(key_value[0], key_value[1]) 

text_dictionary = read_in_file("twain.txt")
print_dictionary(text_dictionary)
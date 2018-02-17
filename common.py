'''
Created on Dec 2, 2017

@author: ITAUser
'''
def countingletters(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True 
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break
        else: 
            if letter == mychar:
                count = count + 1
    print(count)
    return count
import string 
    #make a list with the alphabet 
letters = list(string.ascii_lowercase)
    #make a list to store the value of each letter
letters_count = [0]* 26
    #print(letters_count) 
    #make loop that counts how many of each letter are there
for i in range (len (letters)): 
        letters_count[i] = countingletters("constitution.txt", letters[i])

    #define the maximum value 
print(letters_count)
    #find the letter at the max value
pop = max(letters_count)
print (pop)
    #print the answer 
indexofletter = letters_count.index(pop)
largeletter = letters[indexofletter]
print(lageletter)    
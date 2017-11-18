'''
Created on Nov 18, 2017

@author: ITAUser
'''
#open the text file
#read the file
#split the file
#count the letters
#print result

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
countingletters("constitution.txt", "a")

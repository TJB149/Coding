def d2():#imports system module - needed to end execution
    import sys
    #asks user for name - stored as string
    name = input("Please enter your name: ")
    #asks user how long they sleep - stored as float
    sleep = float(input("Hello "+name+". How many hours per night do you sleep? "))
    #prints how long user sleeps in a week
    print("You sleep "+str(round(sleep*7, 2))+" hours per week")
    #prints how long user sleeps in a month
    print("You sleep "+str(round(sleep*365*4/48, 2))+" hours per month")
    #prints how many days loser sleeps in a month
    print("This equates to roughly "+str(int(sleep*30/24))+" days per month")
    #telling user to press enter to exit
    print("press enter to exit")
    #works by breaking the while loop if an empty string is inputted (meaning that the user just pressed enter)
    while True:   
        name = input()
        if name=="":
            sys.exit()
            break
 



def e2():
   
    #asking for first word
    word1 = input("Please enter your first word: ")
    #asking for second word
    word2 = input("Please enter your second word: ")
    #what is the total number of letters
    print("the total number of letters is "+str(len(word1)+len(word2)))
    #what are the first letters
    print("the first letters are "+word1[0]+" and "+word2[0])
    #what are the last letters
    print("the last letters are "+word1[len(word1)-1] + " and " + word2[len(word2)-1])
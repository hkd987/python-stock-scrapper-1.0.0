from random import choice
name = raw_input("Enter your name : ")
print "Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock"
rps = ['r','p','s']
u = 0
v = 0

#Here is the while loop, which will continue till break. The below text is intended to fit into the while loop.
while 1:
    print "R: Rock,      P: Paper,     S: Scissor"
    user = raw_input("Enter your choice among the three : ")   
    user = user.lower()
    py = choice(rps)

    if user == py:
        print "You chose ",user
        print "I chose ",py
        print "Hence a Tie!"

    elif user == 'r' and py == 's':
        print 'You entered Rock. I had Scissor. You win!'
        u+=1
    elif user == 'r' and py == 'p':
        print 'You entered Rock. I had Paper. You lose!'
        v+=1
    elif user == 's' and py == 'p':
        print 'You entered Scissor. I had Paper. You win!'
        u+=1
    elif user == 's' and py == 'r':
        print 'You entered Scissor. I had Rock. You lose!'
        v+=1
    elif user == 'p' and py == 's':
        print 'You entered Paper. I had Scissor. You lose!'
        v+=1
    elif user == 'p' and py == 'r':
        print 'You entered Paper. I had Rock. You win!'
        u+=1

    if v == 5:
        print 'The Computer Wins!'
        break
    #Provide proper conditions for elif in case user getting 5 points:
    elif u == 5:
        #Congratulate the user on winning along with their name
        print name, 'has won!'
        break
